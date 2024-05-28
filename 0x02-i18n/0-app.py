#!/usr/bin/env/ python3
"""
simple flask application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    A function called when '/'
    is accessed, it will render 'index.html'
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
