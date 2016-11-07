#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: @manojpandey
#
# ..

import os
from flask import (
    Flask,
    render_template
)

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/popularity')
def popularity():
    return render_template('popularity.html')

@app.route('/top10')
def top10():
    return render_template('top10.html')

@app.route('/orig_vs_rt')
def orig_vs_rt():
    return render_template('orig_vs_rt.html')

@app.route('/favorites')
def favorites():
    return render_template('favorites.html')

@app.route('/tweet_type')
def tweet_type():
    return render_template('tweet_type.html')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
