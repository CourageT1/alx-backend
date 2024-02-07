#!/usr/bin/env python3
"""
4-app.py - Flask App with Locale Parameter Support
===================================================

This script sets up a Flask app with support for forcing a particular
locale by passing the 'locale' parameter in the URL.

"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


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


@babel.localeselector
def get_locale():
    """
    Determine the best matched language for the user based on their preferences

    Returns:
        str: Language code for the best matched language.
    """
    # Check if 'locale' parameter is provided in URL and is supported locale
    if 'locale' in request.args and request.args['locale'] in Config.LANGUAGES:
        return request.args['locale']
    else:
        # If not, resort to the previous default behavior
        return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """
    Route function for the homepage.

    Returns:
        str: Rendered HTML content from index.html template.
    """
    return render_template('4-index.html', title=_("home_title"), header=_(
        "home_header"))


if __name__ == '__main__':
    app.run(debug=True)
