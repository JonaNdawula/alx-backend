#!/usr/bin/env python3
"""
This module will Force locale with URL parameter
"""
from flask import Flask, request, render_template_string
from flask_babel import Babel


class Config(object):
    """

    Configuration for Flask-Babel
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


webapp = Flask(__name__)
webapp.config.from_object(Config)
localization = Babel(webapp)


@localization.localeselector
def get_locale() -> str:
    """
    function Documentation
    """
    requested_locale = request.args.get('locale')
    if requested_locale in webapp.config["LANGUAGES"]:
        return requested_locale
    return request.accept_languages.best_match(webapp.config['LANGUAGES'])


@webapp.route('/')
def index() -> str:
    """
    Route Documentation
    """
    return render_template('4-index.html')


if __name__  == "__main__":
    webapp.run(host="0.0.0.0", port='5000')
