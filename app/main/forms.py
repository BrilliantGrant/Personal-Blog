from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField,BooleanField,RadioField,SelectField,FileField,PasswordField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Title',validators=[Required()])
    body =TextAreaField('Content',validators=[Required()])
    category =SelectField('Categories (Optional)', choices=[('pick_up','pick-up '), ('interview Pitch','interview Pitch'),
        ('product pitch', 'product pitch'), ('promotion pitch', 'promotion pitch')])
    submit = SubmitField('Submit')


class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    author =TextAreaField('Author ',validators=[Required()])

    vote = RadioField('Vote',choices=[('upvote','upvote'),('downvote','downvote')],validators=[Required()])                                       
    submit = SubmitField('SUBMIT') 



