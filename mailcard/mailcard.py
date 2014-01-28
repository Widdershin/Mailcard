from __init__ import app, models
from flask import render_template, jsonify


@app.route('/')
def main():
    return render_template("main.html")


@app.route('/api/messages')
def messages():
    unread_messages = {"messages": map(lambda x: x.json,
                                       models.Message.query.all())}

    print unread_messages

    return jsonify(**unread_messages)


def construct_message(message):
    return {"subject": message.subject, "from": dict(*message.sent_from)}


@app.route('/api/messages/update/<user>')
def check_messages(user):
    print "Checking messages for {}".format(user)
    db_user = models.User.query.filter_by(email=user).first_or_404()

    db_user.check_emails()


if __name__ == '__main__':
    app.run(debug=True)
