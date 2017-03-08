from flask import render_template

from . import home


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/addSong')
def addsong():
    """
    Render the add song template on the /addSong route
    """
    return render_template('home/addSong.html', title="Add Song")
    