from wtforms import Form, TextField, PasswordField, validators


class RegistrationForm(Form):
    email = TextField('Email Address', [
        validators.Length(min=6, max=350), validators.Required()
    ])

    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])

    confirm = PasswordField('Repeat Password')


class LoginForm(Form):
    email = TextField('Email Address', [
        validators.Length(min=6, max=350),
        validators.Required()
    ])

    password = PasswordField('Password', [validators.Required()])
