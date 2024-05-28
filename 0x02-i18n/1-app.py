#!/usr/bin/env python3
"""
Module runs simle flask app that
renders a template when root route is accessed
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Configuration class for flask-Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index() -> str:
    """
    This function is called when the root route '/'
   is accessed
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
