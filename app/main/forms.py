from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ReviewForm(FlaskForm):
    title = StringField('Review title', validators=[DataRequired()])
    review = TextAreaField('Bulletin review', validators= [DataRequired()])
    submit = SubmitField('Submit')
