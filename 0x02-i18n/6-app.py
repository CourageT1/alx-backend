#!/usr/bin/env python3
"""
6-app.py - Flask App with User Preferred Locale and Locale Parameter Support
==============================================================================

This script sets up a Flask app with user preferred locale support and locale
parameter support.

"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from babel import Locale

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


# Define a function to get the user's preferred locale
def get_user_locale():
    if g.user:
        user_locale = g.user.get("locale")
        if user_locale in app.config['LANGUAGES']:
            return user_locale
    return None


# Define a get_locale function to determine the best matched language
@babel.localeselector
def get_locale():
    # Check if locale is specified in the URL parameters
    url_locale = request.args.get('locale')
    if url_locale in app.config['LANGUAGES']:
        return url_locale

    # Check if the user has a preferred locale
    user_locale = get_user_locale()
    if user_locale:
        return user_locale

    # Otherwise, use the locale from the request header
    request_locale = request.accept_languages.best_match(
            app.config['LANGUAGES'])
    if request_locale:
        return request_locale

    # Fallback to the default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.before_request
def before_request():
    user_id = int(request.args.get('login_as', 0))
    g.user = get_user(user_id) if user_id else None


class Config:
    """
    Configuration class for the Flask app.
    """

    # Available languages
    LANGUAGES = ["en", "fr"]

    # Set default locale and timezone
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """
    Route function for the homepage.

    Returns:
        str: Rendered HTML content from index.html template.
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
