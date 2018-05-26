from flask import render_template, request, redirect, url_for, flash
from . import main
from ..models import User, Blog, Comment, Email
from flask_login import login_required, current_user
from .. import db, photos
from .forms import BlogForm, CommentForm, EmailForm
from datetime import datetime
import markdown2

@main.route('/')
def index():
    '''
    root function that returns the root page
    '''
    title = 'Home | Beaucar'

    return render_template('index.html', title=title)

@main.route('/create_blog', methods = ['GET','POST'])
@login_required
def create_blog():
    blog_form = BlogForm()

    if blog_form.validate_on_submit():
        blog_title = blog_form.title.data
        blog = blog_form.blog_data.data

        new_blog = Blog(title=blog_title, blog_content = blog, date_posted = datetime.now())
        new_blog.save_blog()

        return redirect(url_for('main.index'))

    return render_template('create_blog.html', title = 'Create Blog', blog_form = blog_form)