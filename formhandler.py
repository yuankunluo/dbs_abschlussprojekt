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
    wrong = []
    news = []
    event = []
    athelets = []
    for k in sorted(req.forms.keys()):
        ks = k.split("_")
        v = req.forms[k]
        ks.append(v)
        ks = [x.strip(" ") for x in ks]
        ks = [x.lower() for x in ks]
        if k.startswith("athelet_"):
            athelets.append(tuple(ks))
            continue
        if k.startswith("event_"):
            event.append(ks)
            continue
        if k.startswith("news_"):
            news.append(ks)
            continue
    # extract information of athelets
    ath_result = {}
    for a in athelets:
        k = a[0]+[1]
        if k not in ath_result.keys():
            ath_result[k] = {}
    for a in athelets:
        ak = a[0]+[1]
        k = a[2]
        v = a[3]
        ath_result[ak][k] = v
    for a in ath_result.keys():
        at = ath_result[a]
        r = db.execute()
    
        
        
        
    
#    s = ""
#    for a in athelets:
#        s += "_".join(a)+"<br>"
#    return s
