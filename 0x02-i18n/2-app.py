#!/usr/bin/env python3
"""
This modul runs a simple flask app that renders
a template when the root route is accessed
"""

from flask import Flast, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration class for
    Flask-Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Will determine the best match
    for supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index() -> str:
    """
    This function is called when the root route is accessed
    """
    return render_template("2-index.html")


if __name__ = "__main__":
    app.run('0.0.0.0', port="5000")
