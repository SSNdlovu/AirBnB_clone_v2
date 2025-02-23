#!/usr/bin/python3
"""Script used to start a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display_hello():
    """Will print hello hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def desplay_hbnb():
    """Will print hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_cText(text):
    """will print C with passed variable"""
    text = text.replace("_", " ")
    return "C %s" % (text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_pythonText(text='is cool'):
    """ A function called with /python/<text> route """
    if text != 'is cool':
        text = text.replace('_', ' ')
    return 'Python %s' % (text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
