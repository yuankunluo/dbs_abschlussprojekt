# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 17:38:53 2014

@author: yuankunluo
"""
import bottle
from bottle import run, Bottle, template
from bottle import static_file
from bottle import request
#from bottle import BaseRequest as request
import os
import web_cgi.contenthandler as ct


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
    result = ct.get_Homepage()
    return template("base", pagetitle = "Homepage", pagecontent = result)

@app.route("/events")
def events():
    result = "events"
    return template("base", pagetitle= "Admin", pagecontent = result)

@app.route("/news")
def news():
    result = "news"
    return template("base", pagetitle= "Admin", pagecontent = result)

@app.route("/sports")
def sports():
    result = "sports"
    return template("base", pagetitle= "Admin", pagecontent = result)

@app.route("/athelets")
def athelets():
    result = "athelets"
    return template("base", pagetitle= "Admin", pagecontent = result)

@app.route("/medalists")
def medalists():
    result = "medalists"
    return template("base", pagetitle= "Admin", pagecontent = result)

@app.route("/admin")
def admin():
    result = "Admin"
    return template("base", pagetitle= "Admin", pagecontent = result)

#==============================================================================
# app
#==============================================================================
run(app,host="127.0.0.1",port=8080)

