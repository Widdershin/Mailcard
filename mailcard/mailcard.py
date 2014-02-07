from __init__ import app, context_io, db
from models import Message
from flask import render_template, jsonify


@app.route('/')
def main():
    return render_template("main.html")

@app.route('/api/messages/update')
def update_messages():
    user_account = context_io.get_accounts(email="ncwjohnstone@gmail.com")[0]
    
    messages = filter(lambda x: Message.query.filter_by(message_id=x.message_id).first() is None, user_account.get_messages()[:3])
    map(lambda x: x.get(), messages)
    new_db_messages = map(lambda x: Message(x.message_id, x.subject, x), messages)
    map(db.session.add, new_db_messages)
    db.session.commit()

    return str(len(new_db_messages))

@app.route('/api/messages')
def messages():

    messages = map(lambda x: x.message, Message.query.all())

    return jsonify(messages=map(construct_message, messages))


def construct_message(message):
    return {"subject": message.subject, "from": message.addresses["from"]}


if __name__ == '__main__':
    app.run(debug=True)
