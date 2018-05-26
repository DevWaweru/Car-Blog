from flask import render_template, request, redirect, url_for, flash
from . import main
from ..models import User, Blog, Comment, Email
from flask_login import login_required, current_user
from .. import db, photos
from .forms import BlogForm, CommentForm, EmailForm
import markdown2

@main.route('/')
def index():
    '''
    root function that returns the root page
    '''
    title = 'Home | Beaucar'

    return render_template('index.html', title=title)

@main.route('/create_blog')
def create_blog():

    return render_template('create_blog.html', title = 'Create Blog')