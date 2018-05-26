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
    all_blogs = Blog.get_all_blogs()

    title = 'Home | Beaucar'

    return render_template('index.html', title=title, all_blogs=all_blogs)

@main.route('/create_blog', methods = ['GET','POST'])
@login_required
def create_blog():
    blog_form = BlogForm()

    if blog_form.validate_on_submit():
        blog_title = blog_form.title.data
        blog = blog_form.blog_data.data

        new_blog = Blog(title=blog_title, blog_content = blog, date_posted = datetime.now())
        new_blog.save_blog()

        return redirect(url_for('main.blog',id=new_blog.id))

    return render_template('create_blog.html', title = 'Create Blog', blog_form = blog_form)

@main.route('/blog/<int:id>')
def blog(id):
    get_blog = Blog.query.get(id)
    if get_blog is None:
        abort(404)

    blog_format = markdown2.markdown(get_blog.blog_content,extras=["code-friendly", "fenced-code-blocks"])

    return render_template('blog.html', blog_format=blog_format, title="Blog")