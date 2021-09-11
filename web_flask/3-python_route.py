#!/usr/bin/python3
"""
This script that starts a Flask web application.

Routes:
/python/(<text>): display “Python ”, followed by the value of
the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”

You must use the option strict_slashes=False in your route definition
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    if '_' in text:
        text = text.replace('_', ' ')
    return 'C %s' % text


@app.route('/python', strict_slashes=False)
def display_python():
    return 'Python is cool'


@app.route('/python/<text>', strict_slashes=False)
def display_pythontext(text):
    if '_' in text:
        text = text.replace('_', ' ')
    return 'Python %s' % text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
