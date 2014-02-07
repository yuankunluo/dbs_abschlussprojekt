# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 17:38:53 2014

@author: yuankunluo
"""
import bottle
from bottle import run, Bottle, template, response
from bottle import static_file
from bottle import request as req
#from bottle import BaseRequest as request
import os
import web_cgi.contenthandler as ct
import web_cgi.formhandler as fh
from bottle import redirect

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
    return template("base",login = check_login(), pagetitle = "Homepage", pagecontent = result)

@app.route("/events")
def events():
    result = ct.get_all_events()
    return template("base",login = check_login(), pagetitle= "All Events", pagecontent = result)

@app.route("/news")
def news():
    result = ct.get_all_news()
    return template("base",login = check_login(), pagetitle= "All News", pagecontent = result)

@app.route("/sports")
def sports():
    result = ct.get_all_sports()
    return template("base",login = check_login(), pagetitle= "All Sports", pagecontent = result)

@app.route("/athletes")
def athletes():
    result = ct.get_all_athletes()
    return template("base",login = check_login(), pagetitle= "All Athletes", pagecontent = result)

@app.route("/medalists")
def medalists():
    result = "medalists"
    return template("base",login = check_login(), pagetitle= "Admin", pagecontent = result)

@app.route("/admin")
def admin():
    uid = req.get_cookie("uid")
    if uid:
        result = uid
        return template("base",login = check_login(), pagetitle= "Admin", pagecontent = result)
    else:
        redirect("/login")
    
@app.route("/search")
def search():
    return template("base",login = check_login(),pagetitle="Search", pagecontent="search")
#==============================================================================
# sigle item page
#==============================================================================
@app.route("/events/<nr:int>")
def view_event(nr):
    """A page for an event
    
    :param nr: An event id
    :type nr: integer
    :returns: A html page for a event
    """
    result, eventname = ct.get_event(nr)
    return template("base",login = check_login(), pagetitle = eventname,pagecontent = result)

#==============================================================================
# add events
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
    check_login(True)
    result = ct.get_add_solo_form(t,nr)
    return template("base",login = check_login(), pagetitle="Add Solo Event", pagecontent = result)

@app.route("/add_solo",method="post")
def add_event_solo_post():
    result = fh.do_add_solo_event(req)
    return template("base",login = check_login(), pagetitle="add solo", pagecontent = result)

@app.route("/add_event/team/<et:re:(p|f|s)>/<tnr:int>/<pnr:int>")
def add_event_team(et,tnr, pnr):
    """Get html form for adding team event
    
    :param t: Event type 
    :type t: string
    :param tnr: Number of teams
    :type tnr: Integer
    :param pnr: Namber of athletes of every team
    :type pnr: Integer
    :returns: Html
    """
    check_login(True)
    result = ct.get_add_team_form(et, tnr, pnr)
    return template("base",login = check_login(),pagetitle="Add Team Event", pagecontent = result)

@app.route("/add_team", method="post")
def add_event_team_post():
    """Process form
    
    """
    result = fh.do_add_team_event(req)
    return template("base",login = check_login(),pagetitle="Add Team Event", pagecontent=result)
#==============================================================================
# add news
#==============================================================================
@app.route("/add_news")
def add_news():
    """Return add news form
    
    """
    check_login(True)
    result = ct.get_add_news_form()
    return template("base",login = check_login(),pagetitle="Add News",pagecontent=result)

@app.route("/add_news",method="post")
def add_news_post():
    """Process the add new form
    
    """
    result = fh.do_add_news(req)
    return template("base",login = check_login(),pagetitle="Add News", pagecontent=result)

def get_user():
    """
    """
    pass
#==============================================================================
# login or singup
#==============================================================================
@app.route("/singup")
def singup():
    """Return a single up form
    
    """
    result = ct.get_singup()
    return template("base",login = check_login(),pagetitle="Sing Up", pagecontent=result)
    
@app.route("/singup",method="post")
def sinup_post():
    uid = fh.do_singup(req)
    response.set_cookie("uid",str(uid))
    redirect("/admin")
    
@app.route("/login")
def login():
    """Get the login form
    
    """
    result = template("login")
    return template("base",login = check_login(),pagetitle="Login", pagecontent=result)

@app.route("/login", method="post")
def login_post():
    """Do the login
    
    """
    result = fh.do_login(req)
    return template("base",login = check_login(),pagetitle="Login", pagecontent=result)

def check_login(auto=False):
    """use cookie to check if login
    
    """
    if auto:
        login = check_login()
        if not login:
            redirect("/login")
    uid = req.get_cookie("uid")
    if uid:
        return True
    else:
        return False
        
@app.route("/logout")
def login_out():
    """Log this user out.
    
    """
    response.set_cookie("uid","")
    redirect("/homepage")

#==============================================================================
# app
#==============================================================================
run(app,host="127.0.0.1",port=8080)

