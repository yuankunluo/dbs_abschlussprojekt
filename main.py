# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 17:38:53 2014

@author: yuankunluo
"""

from bottle import route, run, Bottle

app = Bottle(autojson=True)

@app.route("/") # homepage
def homepage():
    return "Welcome"

run(app,host="127.0.0.1",port=8080)

