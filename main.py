# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 17:38:53 2014

@author: yuankunluo
"""
import bottle
from bottle import run, Bottle, template
from bottle import static_file
from bottle import request as req
#from bottle import BaseRequest as request
import os
import web_cgi.contenthandler as ct
import web_cgi.formhandler as fh

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

@app.route("/events/<nr:int>")
def view_event(nr):
    """A page for an event
    
    :param nr: An event id
    :type nr: integer
    :returns: A html page for a event
    """
    

@app.route("/news")
def news():
    result = "news"
    return template("base", pagetitle= "Admin", pagecontent = result)

@app.route("/sports")
def sports():
    result = "sports"
    return template("base", pagetitle= "Admin", pagecontent = result)

@app.route("/athletes")
def athletes():
    result = "athletes"
    return template("base", pagetitle= "Admin", pagecontent = result)

@app.route("/medalists")
def medalists():
    result = "medalists"
    return template("base", pagetitle= "Admin", pagecontent = result)

@app.route("/admin")
def admin():
    result = "Admin"
    return template("base", pagetitle= "Admin", pagecontent = result)
    
@app.route("/search")
def search():
    return template("base",pagetitle="Search", pagecontent="search")
#==============================================================================
# edit functions
#==============================================================================
@app.route("/add_event/solo/<t:re:(p|f|s)>/<nr:int>")
def add_event_solo(t,nr):
    """Get html form for add solo event
    
    :param t: Event type 
    :type t: string
    :param nr: Number of athlets
    :type nr: Integer
    :returns: Html
    """
    result = ct.get_add_solo_form(t,nr)
    return template("base", pagetitle="add solo", pagecontent = result)

@app.route("/add_solo",method="post")
def add_event_solo_post():
    result = fh.do_add_solo_event(req)
    return template("base", pagetitle="add solo", pagecontent = result)

#==============================================================================
# app
#==============================================================================
run(app,host="127.0.0.1",port=8080)

