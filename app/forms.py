from flask.ext.wtf import Form
from wtforms import TextField ,BooleanField
from wtforms.validators import Required

# from flask.ext.wtf import Form,TextField,BooleanField
# from flask.ext.wtf import Required

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)