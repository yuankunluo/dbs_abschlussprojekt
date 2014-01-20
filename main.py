# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 17:38:53 2014

@author: yuankunluo
"""
import bottle
from bottle import run, Bottle, template
from bottle import static_file
import os
import contenthandler as ct

app = Bottle(autojson=True)
#==============================================================================
# path setting
#==============================================================================
root = os.path.dirname(os.path.abspath(__file__))
viewpath = root + "/views"
bottle.TEMPLATE_PATH.insert(0,viewpath)
#==============================================================================
# static files
#==============================================================================
@app.route("/static/css/<filename>")
def get_css(filename):
    return static_file(filename, root = root + "/static/css")
    
@app.route("/static/images/<filename>")
def get_image(filename):
    return static_file(filename, root = root + "/static/images")


#==============================================================================
# routers
#==============================================================================
@app.route("/homepage")
@app.route("/") # homepage
def homepage():
    result = ct.getHomepage()
    return template("base", pagetitle = "Homepage", pagecontent = result)

@app.route("/events")
def events():
    return "events"


#==============================================================================
# app
#==============================================================================
run(app,host="127.0.0.1",port=8080)

