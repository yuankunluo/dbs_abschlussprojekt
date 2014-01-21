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
import contenthandler as ct
import formhandler as fh


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

#==============================================================================
# edit functions 
#==============================================================================
@app.route("/add_event")
def add_event_form():
    result = ct.get_AddEvent()
    return template("base",pagetitle = "Add Event",
                    pagecontent = result)
                    
@app.route("/add_event",method="POST")
def add_event():
    f = request.forms
    url = request.url
    fh.do_add_event(f, url, "/homepage")


@app.route("/add_news")
def add_news_form():
    result = ct.get_news_form(3)
    return template("base",pagetitle = "Add News",
                    pagecontent = result)
                    
@app.route("/add_news",method="POST")
def add_news():
    r = fh.do_add_news(request)
    return template("base",pagetitle = "Add News",
                    pagecontent = r)

@app.route("/wrong")
def wrong():
    """Return a html, the content is problem tips,
    and a button to go back.
    
    :param content: the html content
    :type content: String
    :param url: the url to go back
    :type url: String
    :returns: a html
    """
    url = request.url
    content = "love me"
    return template("wrong",
                    pagetitle = "Something Wrong",
                    pagecontent = content, url = url)
                    

#==============================================================================
# app
#==============================================================================
run(app,host="127.0.0.1",port=8080)

