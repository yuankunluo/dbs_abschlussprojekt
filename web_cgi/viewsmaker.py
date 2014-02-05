# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 01:55:41 2014

@author: yuankunluo
"""
from bottle import template
from datetime import date

def makeTabele(listOfTuple):
    """Make a html table for a given list of tuple,
    the parameter must be processed by 
    contenthandeler.tupleToList.
    
    :param listOfTuple: A list of tuple, that fits for tablle
    :type listOfTuple: A list
    :returns: A rended tepmlet string
    """
    return template("table",content = listOfTuple)

def makeTableWithLink(r):
    """Make a html table that can automate 
    attatch link to element
    
    :param r: A list of tuple, resulted by contenthandler.tupletolist()
    :type r: A list
    :returns: A rended tepmlet string
    """
    return template("table_with_link", content = r)
#    return result

def makeShortNews(r):
    """Make a html list of short news,
    display the title<link>, first 200 words, pic, time
    
    :param r: A list of tuple, resulted by contenthandler.tupletolist()
    :type r: A list
    :returns: A rended tepmlet string
    """
    return template("news_short", content = r)
    
def makeSelector(r , options_only=False):
    """Make a html form select.
    
    :param r: A list of tuple, resulted by contenthandler.tupletolist()
    :type r: A list
    :returns: A rended tepmlet string
    """
    if options_only:
        return template("select_option", content=r)
    return template("select", content = r)
#==============================================================================
# make a Year, Date, Time, Selector    
#==============================================================================
def rangeSelector(t="year", options_only=False, name="year", label="year"):
    """Make a Year, Date, Time select
    
    :param t: A type to select ["year","month","day","hour","minute"]
    :type t: Sting
    :param name: A name attrbute
    :type name: String
    :param label: A label for the selector
    :type label: String
    :param options_only: A toggle to speicify if just ouput option
    :type options_only: Boolean
    :returns: A html selector
    """
    if options_only:
        temp = "select_range_option"
    else:
        temp = "select_range"
    if t == "year":
        cur_year = date.today().year
        min_year = cur_year - 100
        cur_year = cur_year - 18
        options = range(min_year, cur_year)
    if t == "month":
        options = range(1,13)
    if t == "day":
        options = range(0,32)
    if t == "hour":
        options = range(0,25)
    if t == "minute":
        options = range(0,56,5)
    return template(temp,name=name,label=label,options=options)                

    
    
    
    
    
    