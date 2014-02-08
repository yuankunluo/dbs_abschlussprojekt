# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:35:29 2014

@author: yuankunluo
"""
import dbconnector as db
import sqlstaments as sqls
import viewsmaker as vm
from bottle import template
from bottle import redirect,response,request
import formhandler as fh
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
    lastEvents = db.fetch_tuple(sqls.lastthreeevents,None,True)
    t = vm.makeTableWithLink(lastEvents)
    # get news
    n = db.fetch_tuple(sqls.hotnews)
    n = vm.makeShortNews(n)
    pagecontent = template("index", table = t , news = n)
    return pagecontent
#==============================================================================
# add news
#==============================================================================
def get_add_news_form(uid):
    """Return a form for add news
    
    :param uid: The user id stored in cookies
    :tyoe uid: String
    :returns: a html form for adding news
    """
    # make selector for events
    eo = db.fetch_tuple(sqls.events_option) 
    eo = vm.makeSelector(eo,True)
    return template("add_news",uid= uid, event_options=eo)
#==============================================================================
# add solo event
#==============================================================================
def get_add_solo_form(et,number,uid):
    """Return a from for adding solo event.
    
    :param et: Event type
    :type et: String
    :param number: The number of athelets 
    :type number: Integer
    :param uid: The user id stored in cookies
    :tyoe uid: String
    :returns: a html form for add event
    """
    # get selector options
    countries = db.fetch_tuple(sqls.select_countries)
    co = vm.makeSelector(countries, True)
    vanues = db.fetch_tuple(sqls.select_vanues)
    vo = vm.makeSelector(vanues, True)
    sports = db.fetch_tuple(sqls.select_sports)
    so = vm.makeSelector(sports, True)
    events = db.fetch_tuple(sqls.select_events)
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
                    year_options = yo,
                    uid = uid)

def get_add_team_form(et,tnr,pnr, uid):
    """Get a html form for adding team event.
    
    :param et: the type of a event [p,s,f]
    :type et: a sting
    :param tnr: the number of teams
    :type tnr: a integer
    :param pnr: the number of every team
    :type pnr: a integer
    :param uid: The user id stored in cookies
    :tyoe uid: String
    :returns: a html form
    """
     # get selector options
    countries = db.fetch_tuple(sqls.select_countries)
    co = vm.makeSelector(countries, True)
    vanues = db.fetch_tuple(sqls.select_vanues)
    vo = vm.makeSelector(vanues, True)
    sports = db.fetch_tuple(sqls.select_sports)
    so = vm.makeSelector(sports, True)
    events = db.fetch_tuple(sqls.select_events)
    eo = vm.makeSelector(events, True)
    # get datetime options
    yo = vm.rangeSelector("year",True)
    mto = vm.rangeSelector("month",True)
    do = vm.rangeSelector("day", True)
    ho = vm.rangeSelector("hour",True)
    mo = vm.rangeSelector("minute", True)
    # return html form
    return template("add_event_team", et = et,
                    event_options = eo,
                    vanue_options = vo,
                    sports_options = so,
                    month_options = mto,
                    day_options = do,
                    hour_options = ho,
                    minute_options = mo,
                    country_options = co,
                    year_options = yo,
                    tnr = tnr,
                    pnr = pnr, uid = uid)
#==============================================================================
# event page   
#==============================================================================
def get_event(nr):
    """Get the html content of for a given event
    
    :prama nr: A event id
    :type nr: integer
    :returns: a html content , a event name for display as title
    """
    # template variable
    event_table = db.fetch_tuple(sqls.event_page_eventinfo, (nr,), True)
    if len(event_table) < 1:
        error = template("error", error = "Event was not in db.")
        return error, "Event"
    event_name = event_table[1][0]
    event_table = vm.makeTableWithLink(event_table)
    result = event_table
    results_table = db.fetch_tuple(sqls.event_results_table, (nr,),True)
    results_table = vm.makeTableWithLink(results_table)
    news_table = db.fetch_tuple(sqls.event_news_table, (nr,),True)
    news_table = vm.makeTableWithLink(news_table)
    result = template("eventpage", 
                      event_name = event_name,
                      news_table = news_table,
                      event_table= event_table, 
                      results_table=results_table)
    return result, event_name
    
def get_all_events():
    """Make a tables for events page
    
    """
    solo = db.fetch_tuple(sqls.select_all_solo_events,None,True)
    solo = vm.makeTableWithLink(solo)
    team = db.fetch_tuple(sqls.select_all_team_events,None,True)
    team = vm.makeTableWithLink(team)
    result = "<h2>solo events</h2>" + solo
    result += "<h2>team events</h2>" + team
    result = template("content_with_h1",h1="All Events",content = result)
    return result

#==============================================================================
# Add page content
#==============================================================================
def get_admin():
    """Make a admin page
    
    """
    u_id = request.get_cookie("uid")
    u_name = db.select_something("users",("name",),{"id":u_id})[1][0]
    a_op = db.fetch_tuple(sqls.a_options)
    a_op = vm.makeSelector(a_op,True)
    n_op = db.fetch_tuple(sqls.n_options)
    n_op = vm.makeSelector(n_op,True)
    return template("admin", u_name = u_name, isreporter=fh.check_reporter(),
                    n_options= n_op, a_options = a_op)
    
#==============================================================================
# news pages
#==============================================================================
def get_all_news():
    """Make a table for all news
    
    """
    e_news = db.fetch_tuple(sqls.select_all_event_news,None, True)
    e_news = vm.makeTableWithLink(e_news)
    ne_news = db.fetch_tuple(sqls.select_all_non_event_news,None, True)
    ne_news = vm.makeTableWithLink(ne_news)
    news = """<h2>All Events News</h2>""" + e_news
    news += """<h2>All other news</h2>""" + ne_news
    result = template("content_with_h1", h1="All News", content = news)
    return result
#==============================================================================
# sports pages
#==============================================================================
def get_all_sports():
    """Make a table for all sports
    
    """
    sports = db.fetch_tuple(sqls.select_all_sports, None, True)
    sports = vm.makeTableWithLink(sports)
    result = template("content_with_h1",h1="All Sports", content = sports)
    return result
#==============================================================================
# athletes pages
#==============================================================================
def get_all_athletes():
    """Make a table for all ahletes
    
    """
    athletes = db.fetch_tuple(sqls.select_all_athletes, None, True)
    athletes = vm.makeTableWithLink(athletes)
    result = template("content_with_h1",h1="All Athletes", content = athletes)
    return result
#==============================================================================
# uploader
#==============================================================================
def get_upload_pic(table, iid):
    """Make a upload form
    
    :param table: the table name in db, must be [athletes, users, news]
    :type table: string
    :param iid: the item id primary key in db
    :type iid: integer
    :returns: a html form
    """
    fh.check_login()
    uid = request.get_cookie("uid")
    return template("upload_pic",table=table, iid = iid, uid = uid)
#==============================================================================
# singup and login
#==============================================================================
def get_singup():
    """Return a singup form
    
    :returns: a html form
    """
    yo = vm.rangeSelector("year",True)
    mto = vm.rangeSelector("month",True)
    do = vm.rangeSelector("day", True)
    countries = db.fetch_tuple(sqls.select_countries)
    co = vm.makeSelector(countries, True)
    return template("singup", 
                    month_options = mto,
                    day_options = do,
                    country_options = co,
                    year_options = yo)

    