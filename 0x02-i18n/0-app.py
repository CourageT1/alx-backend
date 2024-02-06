#!/usr/bin/env python3
"""
0-app.py - Basic Flask App
===========================

This script sets up a basic Flask app with a single route ("/") and
an index.html template.
The route renders the index.html template, which displays a page title
"Welcome to Holberton"
and a header "Hello world".

"""

from flask import Flask, render_template

app = Flask(__name__)


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
