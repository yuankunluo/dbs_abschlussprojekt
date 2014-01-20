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

sportsselect = "select s.name as sport, s.id as sports_link \
from sports s"
