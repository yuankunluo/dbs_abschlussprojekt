# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 01:55:41 2014

@author: yuankunluo
"""
from bottle import template

def makeTabelle(listOfTuple):
    """Make a html tablle for a given list of tuple,
    the parameter must be processed by 
    contenthandeler.tupleToList.
    
    :param listOfTuple: A list of tuple, that fits for tablle
    :type listOfTuple: A list
    :returns: A rended tepmlet string
    """
    return template("table",content = listOfTuple)