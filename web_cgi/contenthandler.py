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
# add solo event
#==============================================================================
def get_add_solo_form(et,number):
    """Return a from for adding solo event.
    
    :param et: Event type
    :type et: String
    :param number: The number of athelets 
    :type number: Integer
    :returns: a html form for add event
    """
    # get selector options
    countries = db.execute(sqls.select_countries)
    co = vm.makeSelector(countries, True)
    vanues = db.execute(sqls.select_vanues)
    vo = vm.makeSelector(vanues, True)
    sports = db.execute(sqls.select_sports)
    so = vm.makeSelector(sports, True)
    events = db.execute(sqls.select_events)
    eo = vm.makeSelector(events, True)
    # get datetime options
    yo = vm.rangeSelector("year",True)
    mto = vm.rangeSelector("month",True)
    do = vm.rangeSelector("day", True)
    ho = vm.rangeSelector("hour",True)
    mo = vm.rangeSelector("minute", True)
    # return html form
    return template("add_event_solo", et = et, ath_number = range(1,number+1),
                    event_options = eo,
                    vanue_options = vo,
                    sports_options = so,
                    month_options = mto,
                    day_options = do,
                    hour_options = ho,
                    minute_options = mo,
                    country_options = co,
                    year_options = yo)
#==============================================================================
# event page   
#==============================================================================
def get_event(nr):
    """Get the html content of for a given event
    
    :prama nr: A event id
    :type nr: integer
    :returns: a html content
    """
    
    
    
    
