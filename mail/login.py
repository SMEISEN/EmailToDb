from mail import m, emailConfig

_email_user = emailConfig.EMAIL_USER
_email_pass = emailConfig.EMAIL_PASS

m.login(_email_user, _email_pass)
