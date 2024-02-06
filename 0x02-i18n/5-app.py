#!/usr/bin/env python3
"""
5-app.py - Flask App with User Login Emulation and Personalized Messages
=========================================================================

This script sets up a Flask app with user login emulation and personalized
messages.

"""

from flask import Flask, render_template, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

# Define the user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


# Define a function to get the user based on user ID
def get_user(user_id):
    return users.get(user_id)


# Define a before_request function to fetch the user information
@app.before_request
def before_request():
    user_id = int(request.args.get('login_as', 0))
    g.user = get_user(user_id) if user_id else None


@app.route('/')
def index():
    """
    Route function for the homepage.

    Returns:
        str: Rendered HTML content from index.html template.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
