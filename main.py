# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 17:38:53 2014

@author: yuankunluo
"""
import bottle
from bottle import route, run, Bottle, template
from bottle import SimpleTemplate as Tpl
import os

path = os.path.dirname(os.path.abspath(__file__))+"/views/"
# change template folder
bottle.TEMPLATE_PATH.insert(0,'path')

app = Bottle(autojson=True)

@app.route("/") # homepage
def homepage():
    return "hello world"

run(app,host="127.0.0.1",port=8080)

