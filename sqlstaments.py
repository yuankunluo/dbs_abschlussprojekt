# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 01:37:36 2014

@author: yuankunluo
"""
#==============================================================================
# home page
#==============================================================================
with open("static/sqls/lastevents", "rb") as f:
    lastthreeevents = f.read()

with open("static/sqls/hotnews", "rb") as f:
    hotnews = f.read()

with open("static/sqls/select_vanues", "rb") as f:
    select_vanues = f.read()

with open("static/sqls/select_events", "rb") as f:
    select_events = f.read()
    
with open("static/sqls/select_sports", "rb") as f:
    select_sports = f.read()
    
with open("static/sqls/select_countries", "rb") as f:
    select_countries = f.read()
#==============================================================================
# add news   
#==============================================================================
with open("static/sqls/insert_athelet", "rb") as f:
    insert_athelet = f.read()


sportsselect = "select s.name as sport, s.id as sports_link \
from sports s"
