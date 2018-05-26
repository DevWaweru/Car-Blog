from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    blog_data = TextAreaField('Type Blog here', validators=[Required()])
    post = SubmitField('Post Blog')

class CommentForm(FlaskForm):
    name = StringField('Name',validators=[Required()])
    email = StringField('Email', validators=[Required()])
    comment_data = TextAreaField('Enter Comment', validators=[Required()])
    post = SubmitField('Post Comment')

class EmailForm(FlaskForm):
    name = StringField('First Name', validators=[Required()])
    email = StringField('Email', validators=[Required()])
    subscribe = SubmitField('Subscribe')