# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:35:29 2014

@author: yuankunluo
"""
import dbconnector as db
import sqlstaments as sqls
import viewsmaker as vm
from bottle import template

def getHomepage():
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


        
    
    
    
    
    
