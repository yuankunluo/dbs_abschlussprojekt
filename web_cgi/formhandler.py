# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:35:43 2014

@author: yuankunluo
"""

import dbconnector as db
from bottle import redirect
import sqlite3


def do_add_solo_event(req):
    """"Do sql insert based on the html form
    
    :prame req: The request object
    :tyeoe req: bottle.request
    :returns: none
    """
    form = req.forms
    infos = []
    for k,v in form.items():
        k = k.split("_")
        k.append(v.strip(" "))
        infos.append(tuple(k))
    infos = sorted(infos, key=lambda info:info[0])
    infos = manage_tuples(infos)
    # test if the event was already in db
    if db.test_already("events",{"name":infos["event"]["name"],}):
        oid = db.select_something("events","oid",{"name":infos["event"]["name"],})
        oid = oid[0][0]
        error = '<h1>Error:</h1>Event was already reported, please go to <a class="wrong" href="../edit_event/{oid}">edit event</a>'
        error += " to edit this event."        
        return error.format(oid= oid)
    else:
        return infos

#==============================================================================
# help functions
#==============================================================================
def manage_tuples(tuples):
    """Helper to make the request tuples into wellformated tuple,
    inorder to match tablls in dbs
    
    :param tuples: a list of tuples
    :type tuples: a list
    :returns: a list of tuples that match tables in dbs
    """
    tables = {}
    for t in tuples:
        s = t[2]
        if t[1] in ["month","year","day","hour","minute"] and len(s) ==1:
            s = "0" + s
        if t[0] not in tables.keys():
            tables[t[0]] = {}
            tables[t[0]][t[1]]=s
        else:
            tables[t[0]][t[1]]=s   
    return tables
        
        