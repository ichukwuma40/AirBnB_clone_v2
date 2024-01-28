#!/usr/bin/python3
""" 0. This  is Script to start a Flask web application """

from flask import Flask


app = Flask(__name__)

# Define the route for the root URL /

@app.route('/', strict_slashes=False)
def hello_world():
    """ Displys text. """
    return 'Hello HBNB!'

if __name__ == '__main__':

# Start the flask development server
# Listern on all available network interface

    app.run(host='0.0.0.0', port=5000)
