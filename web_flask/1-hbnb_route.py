#!/usr/bin/python3
"""A script that starts a Flask web application"""


from flask import Flask


app = Flask("__name__")


@app.route("/", strict_slashes=False)
def root_HBNB():
    """View function for home page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """View for hbnb page"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
