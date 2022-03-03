from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class SourceForm(FlaskForm):

    title = StringField('Source title',validators=[Required()])
    source= TextAreaField('News source', validators=[Required()])
    submit = SubmitField('Submit')