from __init__ import app, context_io, db, models, login_manager, forms
from flask import render_template, jsonify, redirect, url_for
from flask.ext.login import login_user, login_required


@app.route('/')
@login_required
def main():
    return render_template("main.html")


@app.route('/api/messages/update', methods=['POST'])
def update_messages():
    user_account = context_io.get_accounts(email="ncwjohnstone@gmail.com")[0]

    messages = filter(lambda x: models.Message.query.filter_by(
                      message_id=x.message_id).first() is None,
                      user_account.get_messages()[:10])
    map(lambda x: x.get(), messages)
    new_db_messages = map(lambda x: models.Message(
                          x.message_id, x.subject, x), messages)
    map(db.session.add, new_db_messages)
    db.session.commit()

    return str(len(new_db_messages))


@app.route('/api/messages')
def messages():
    messages = map(lambda x: x.message, models.Message.query.all())
    return jsonify(messages=map(construct_message, messages))


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = forms.LoginForm()

    if form.validate_on_submit():
        user = models.User.query.filter_by(
            email=form.email.data).first_or_404()

        if user.check_password(form.password.data):
            login_user(user)

        return redirect('/')

    return render_template("login.html", form=form)


def construct_message(message):
    return {"subject": message.subject, "from": message.addresses["from"]}


@login_manager.user_loader
def load_user(userid):
    return models.User.query.get(int(userid))
