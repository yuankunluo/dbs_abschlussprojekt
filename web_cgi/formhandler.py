# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:35:43 2014

@author: yuankunluo
"""

import dbconnector as db
from bottle import redirect
import sqlite3
import re
from bottle import template
#==============================================================================
# add solo event
#==============================================================================
def do_add_solo_event(req):
    """"Do sql insert based on the html form
    
    :prame req: The request object
    :tyeoe req: bottle.request
    :returns: none
    """
    form = req.forms
    infos = request_to_dict(form)
    ts = {"p":"Preliminaries","s":"Semifinal","f":"Finals"}
    # collect event infomation
    e_condition = infos["event"]
    e_condition["name"] = e_condition["name"] + " -- "+ ts[e_condition["type"]]
    test = db.select_something("events",("id","name"),{"name":e_condition["name"]})
    e_name = e_condition["name"]
    if len(test) > 1:
        return error_duplicate(test,e_name,"events")
    # collect ath infos
    ath_keys = [ath for ath in infos.keys() if ath.startswith("ath")]
    p_infos = {}
    ath_rowids = []
    for ak in ath_keys:
        a_info = infos[ak]
        a_condition = {"firstname":a_info["firstname"],
        "lastname":a_info["lastname"],
        "gender":a_info["gender"],
        "country":a_info["country"],
        "birthday":a_info["date"],}
        ath_rowid = db.insert_into_tables("athletes",a_condition, ("rowid",))[1][0]
        ath_rowids.append(ath_rowid)
        p_condition = {"athlete":ath_rowid,"rank":a_info["rank"],
                       "result":a_info["result"],"medal":a_info["medal"]}
        p_infos[ath_rowid] = p_condition
    ath_rowids_rm = remove_duplicates(ath_rowids)
    # test if duplicated athe in one event
    if len(ath_rowids) != len(ath_rowids_rm):
        e = "You have inputed duplicated althetes in one event!"
        return template("error",error = e)
    e_id =  db.insert_into_tables("events",e_condition,("id",))[1][0]
    for k,v in p_infos.items():
        v["event"] = e_id
        db.insert_into_tables("participants",v,("rowid",))
    redirect("/events/"+str(e_id))
#==============================================================================
# add team event
#==============================================================================
def do_add_team_event(req):
    """Process the form for adding team event
    
    :param req: a html post request
    :type req: a bottle.request
    :returns: none
    """
    # clean form request
    form = request_to_dict(req.forms)
    event = form.pop("event")
    ts = {"p":"Preliminaries","s":"Semifinal","f":"Finals"}
    # test if this event in db
    e_name = event.pop("name")
    e_name = e_name + " (team) -- " + ts[event["type"]]
    event["name"] = e_name
    e_test = db.select_something("events",("rowid",),{"name":e_name})
    if len(e_test) > 1:
        return error_duplicate(e_test,e_name,"events")
    # add athletes
    teams = extract_from_interdict(form)
    
    # add event
    e_id = db.insert_into_tables("events", event,("id",))
    return event, teams
#==============================================================================
# help functions
#==============================================================================
def request_to_dict(reqForms):
    """Helper: transform a bottle.request.form into dict
    
    :param reqForms: a bottle.request.form
    :type reqForms: form object
    :returns: a dict of {"tuplehead":{"column":"value"}}
    """
    infos = []
    for k,v in reqForms.items():
        k = k.split("_")
        k.append(v)
        k = cleanRequest(k)
        infos.append(tuple(k))
    infos = manage_tuples(infos)
    return infos
    
def manage_tuples(tuples):
    """Helper: make the request tuples into wellformated tuple,
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
    # make date
    for k in tables.keys():
        t = tables[k]
        if "year" in t.keys():
            year = t["year"]
            month = t["month"]
            day = t["day"]
            date = "-".join([year,month,day])
            t.pop("year")
            t.pop("month")
            t.pop("day")
            t["date"] = date
        if "minute" in t.keys():
            hour = t["hour"]
            minute = t["minute"]
            time = ":".join([hour,minute])
            t.pop("hour")
            t.pop("minute")
            t["time"] = time
    return tables

def cleanRequest(sqltupe):
    """Helper: clean sql
    
    :param sqltupe: A quests data extracted
    :type sqltupe: A list
    :returns: A list
    """
    result = []
    for i in sqltupe:
        i = i.lower()
        i  = re.sub(r"select.*from|insert into|update .* wherer|delete .* from","",i)
        i = i.strip(" ")
        result.append(i)
    return result
    
def remove_duplicates(l):
    """Remove duplicate element in a list
    
    :param l: A list object
    :type l: List
    :returns: a list without duplicate
    """
    return list(set(l))

def extract_from_interdict(interdict, delimeter="/"):
    """Extract ath for every team. It can handel inter delimeter "/".
    The add team event form results a dict like:
    {"t1":{"a1/firstname":"love", "a2/gender":"f"}}.
    This helper make the inter infomations into a inter dict:
    Result:
    {"t1":{"r":"100", "medal":"g","a1":{"firstname":"love"},"a2":{"gender":"f"}}}
    
    :param teams: A dict of teams like {teams:{athx/xx:xxx, athx/xx:xxx}
    :type teams: A dict
    :returns: A dict 
    """
    result = {}
    for k,v in interdict.items():
        result[k] = {}
        for ik, iv in v.items():
            # split ik,iv into one list [k, k2, v]
            ks = ik.split(delimeter)
#            print(type(ks))
            ks.append(iv)
            temp = ks
#            print(temp)
            if len(temp) == 2:
                result[k][temp[0]] = temp[1]
                continue
            if temp[0] in result[k].keys() and len(temp)>2:
                result[k][temp[0]][temp[1]] =  temp[2]
            else:
                result[k][temp[0]] = {}
                result[k][temp[0]][temp[1]] = temp[2]
    return result

def error_duplicate(e_test,item="event_1", link="events"):
    """Return a error page for duplicate event 
    
    :param event_test: a result of test by db.select_something()
    :type event_test: a list of tuple
    :param itemname: a name for given item
    :type itemname: a string
    :param link: a link goal to the duplicate 
    :type link: string
    :returns: String
    """
    e_rowid = e_test[1][0]
    e = """
    <a class="wrong" href="/{link}/{oid}">{itemname}</a> was already reported!
    please go to <a class="wrong" href="/edit_event/{oid}">edit event</a>to edit this event.
    """
    e = e.format(oid = e_rowid, itemname = item, link = link)
    return template("error", error = e)