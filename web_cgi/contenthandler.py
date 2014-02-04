# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:35:29 2014

@author: yuankunluo
"""
import dbconnector as db
import sqlstaments as sqls
import viewsmaker as vm
from bottle import template
#==============================================================================
# homepage
#==============================================================================
def get_Homepage():
    """Get the content for homepage.
    
    – Anzeigen der letzten drei stattgefundenen Wettkampfe.
    – Anzeigen aller Wettkampfberichte einer Disziplin.
    – Anzeigen von Wettkampfen, 
    bei denen von bestimmten Nationen Medaillen erzielt wurden.
    
    :returns: rederned String
    """
    pagecontent = None
    # get table for last 3 events
    lastEvents = db.execute(sqls.lastthreeevents)
    t = vm.makeTabele(lastEvents)
    # get news
    n = db.execute(sqls.hotnews, True)
    n = vm.makeShortNews(n)
    pagecontent = template("index", table = t , news = n)
    return pagecontent
#==============================================================================
# add event
#==============================================================================
def get_AddEvent():
    """Return a html page for adding new event
    
    :returns: A html for adding new event
    """
    # get select_sports
    s = db.execute(sqls.select_sports)
    s = vm.makeSelector(s)
    # get select_events
    e = db.execute(sqls.select_events)
    e = vm.makeSelector(e)
    # get select_vanues
    v = db.execute(sqls.select_vanues)
    v = vm.makeSelector(v)
    add_form = template("add_event",select_events = e,
                        select_sports = s,
                        select_vanues = v)
    return add_form
    
#==============================================================================
# news form
#==============================================================================
def get_news_form(n):
    """Return a html form for adding news.
    
    :param n: The number of athelets
    :type n: Integer
    :returns: A html form
    """
    # get select_sports
    s = db.execute(sqls.select_sports)
    s = vm.makeSelector(s,True)
    # get select_events
    e = db.execute(sqls.select_events)
    e = vm.makeSelector(e,True)
    # get select_vanues
    v = db.execute(sqls.select_vanues)
    v = vm.makeSelector(v,True)
    # get select_countries
    c = db.execute(sqls.select_countries)
    c = vm.makeSelector(c, True)
    news_form = template("add_news",
                        select_events = e,
                        select_sports = s,
                        select_vanues = v,
                        select_countries = c,
                        numberofathelets = n)
    return news_form
#==============================================================================
# admin_page
#==============================================================================
def admin():
    """Return admin page.
    
    
    """
        
    
    
    
    
    
