#!/usr/bin/python3
"""
This script starts a Flask web application.

Routes:
/hbnb: display “HBNB”.

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)