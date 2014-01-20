# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 01:37:36 2014

@author: yuankunluo
"""
#==============================================================================
# home page
#==============================================================================
lastthreeevents = "select e.name, e.date, e.time, v.name as vanue, \
s.name as sport \
from events e, vanues  v, sports s \
where e.vanue = v.id and e.sport = s.id \
order by e.date , e.time \
limit 3"