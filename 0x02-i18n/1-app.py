#!/usr/bin/env python3
"""
file: 1-app
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """configration file"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/")
def index():
    """display the hello world message"""
    return render_template("1-index.html")

if __name__ == "__main__":
    app.run(debug=True)
