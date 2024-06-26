#!/usr/bin/env/ python3
"""
simple flask application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    A function called when '/'
    is accessed, it will render '0-index.html'
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
