#!/usr/bin/env python3
"""
app.py - Flask App with Timezone Selection Support
=====================================================

This script sets up a Flask app with timezone selection support.

"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz


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


# Define a function to get the user's preferred timezone
def get_user_timezone():
    if g.user:
        user_timezone = g.user.get("timezone")
        if user_timezone:
            try:
                pytz.timezone(user_timezone)
                return user_timezone
            except pytz.exceptions.UnknownTimeZoneError:
                pass
    return "UTC"


# Define a get_timezone function to determine the best matched timezone
@babel.timezoneselector
def get_timezone():
    # Check if timezone is specified in the URL parameters
    url_timezone = request.args.get('timezone')
    if url_timezone:
        try:
            pytz.timezone(url_timezone)
            return url_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Check if the user has a preferred timezone
    user_timezone = get_user_timezone()
    if user_timezone:
        return user_timezone

    # Fallback to UTC
    return "UTC"


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
    return render_template('index.html')


def get_current_time():
    return datetime.datetime.now(pytz.timezone(get_timezone()))


if __name__ == '__main__':
    app.run(debug=True)
