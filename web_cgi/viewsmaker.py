# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 01:55:41 2014

@author: yuankunluo
"""
from bottle import template

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
    
def makeSelector(r, options_only=False):
    """Make a html form select.
    
    :param r: A list of tuple, resulted by contenthandler.tupletolist()
    :type r: A list
    :returns: A rended tepmlet string
    """
    if options_only:
        return template("select_option", content=r)
    return template("select", content = r)
                
            
        
    
    
    
    
    
    