#!/usr/bin/env python3
"""
This module emulates a user login by usin a mock database
"""
from flask import Flask, render_template, request, g
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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
    """
    Get a user from 'users' table by ID
    """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@webapp.before_request
def before_request():
    """
    Function to be executed first
    """
    user = get_user()
    g.user = user


@localization.localeselector
def get_locale() -> str:
    """
    Selects the best matching language for the user
    """
    locale = request.args.get('locale')
    if locale and locale in webbapp.config["LANGUAGES"]:
        return locale

    if g.get('user') and g.user['locale'] in webapp.config["LANGUAGES"]:
        return g.user['locale']
    locale = request.accept_languages.best_match(webapp.config['LANGUAGES'])
    if locale:
        return locale

    return web.config["BABEL_DEFAULT_LOCALE"]

@localization.timezoneselector
def get_timezone():
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimezoneError:
            pass

        if g.get('user'):
            return g.user['timezone']

        return webapp.config['BABEL_DEFAULT_TIMEZONE']



@webapp.route('/')
def index() -> str:
    """
    Render the index page
    """
    return render_template('7-index.html')


if __name__ == "__main__":
    webapp.run(host="0.0.0.0", port=5000)
