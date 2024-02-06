#!/usr/bin/env python3
"""
3-app.py - Flask App with Internationalization (i18n) using Flask-Babel
========================================================================

This script sets up a Flask app with internationalization support using
Flask-Babel.

"""

from flask import Flask, render_template
from flask_babel import Babel, _

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
    Determine the best matched language for the user based on their
    preferences.

    Returns:
        str: Language code for the best matched language.
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """
    Route function for the homepage.

    Returns:
        str: Rendered HTML content from index.html template.
    """
    return render_template('3-index.html', title=_(
        "home_title"), header=_("home_header"))


if __name__ == '__main__':
    app.run(debug=True)
