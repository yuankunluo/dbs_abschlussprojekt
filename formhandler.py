# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:35:43 2014

@author: yuankunluo
"""

import dbconnector as db
from bottle import redirect
import sqlite3

def do_add_event(form, url,  goto):
    """Do sql insertion based on the html form.
    
    :param form: A html form posted information.
    :type form: A bottle.request.forms object
    :param url: the request url
    :type url: string
    :param goto: Specify the next step after db update
    :type goto: A string
    :returns: none
    """
    redirect(goto)

def do_add_news(req):
    """"Do sql insert based on the html form
    
    :prame req: The request object
    :tyeoe req: bottle.request
    :returns: none
    """
    news = []
    event = []
    athelets = []
    
#    for k in sorted(req.forms.keys()):
#        s += "{k} => {v}<br>".format(k=k,v=req.forms[k])
#        print(s)
    return s
