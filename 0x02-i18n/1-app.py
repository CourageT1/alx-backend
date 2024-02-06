#!/usr/bin/env python3
"""
0-app.py - Basic Flask App with Babel Extension
================================================

This script sets up a basic Flask app with Babel extension.
It also configures available languages and sets the default locale and
timezone.

"""

from flask import Flask, render_template
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


@app.route('/')
def index():
    """
    Route function for the homepage.

    Returns:
        str: Rendered HTML content from index.html template.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
