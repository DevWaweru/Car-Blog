from flask import render_template, request, redirect, url_for
from . import main

@main.route('/')
def index():
    '''
    root function that returns the root page
    '''
    title = 'Home | Beaucar'

    return render_template('index.html', title=title)