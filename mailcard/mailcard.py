from __init__ import app, context_io
from flask import render_template, jsonify


@app.route('/')
def main():
    return render_template("main.html")


@app.route('/api/messages')
def messages():
    user_account = context_io.get_accounts(email="ncwjohnstone@gmail.com")[0]

    messages = user_account.get_messages()[:2]

    map(lambda x: x.get(), messages)

    print messages
    print messages[0].subject, messages[0].addresses

    print map(construct_message, messages)

    return jsonify(messages=map(construct_message, messages))


def construct_message(message):
    return {"subject": message.subject, "from": message.addresses["from"]}


if __name__ == '__main__':
    app.run(debug=True)
