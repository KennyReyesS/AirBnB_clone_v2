#!/usr/bin/python3
"""
This script starts a Flask web application.

Route:
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY.

You must use the option strict_slashes=False in your route definition
"""


from flask import Flask, render_template


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


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    if type(n) == int:
        return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_n_html(n):
    if type(n) == int:
        return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
