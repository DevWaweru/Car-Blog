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

    all_blogs = Blog.get_all_blogs()
    if all_blogs:
        blogs = all_blogs
        return render_template('index.html', title=title, all_blogs=blogs )
    elif not all_blogs:
        blog_message = 'Whoooops, we have no blogs here'
        return render_template('index.html', title=title, blog_message = blog_message)


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

@main.route('/blog/<int:id>', methods=['GET','POST'])
def blog(id):
    get_blog = Blog.query.get(id)
    if get_blog is None:
        abort(404)

    blog_format = markdown2.markdown(get_blog.blog_content,extras=["code-friendly", "fenced-code-blocks"])

    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        user_name = comment_form.name.data
        user_email = comment_form.email.data
        user_comment = comment_form.comment_data.data

        new_comment = Comment(name=user_name,email=user_email,comment_content=user_comment,date_comment = datetime.now(),blog_id=id)
        new_comment.save_comment()

        return redirect(url_for('main.blog',id=id))
    
    get_comments = Comment.get_blog_comments(id)

    return render_template('blog.html', blog_format=blog_format, title="Blog", comment_form=comment_form, get_comments=get_comments)