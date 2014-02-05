# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 01:37:36 2014

@author: yuankunluo
"""
#==============================================================================
# home page
#==============================================================================
lastthreeevents = """
select e.name as event, e.date, e.time, v.name as vanue,
s.name as sport
from events e, vanues  v, sports s 
where e.vanue = v.id and e.sport = s.id 
order by e.date , e.time
limit 3
"""

#==============================================================================
# home page
#==============================================================================
hotnews = """
select n.title as title,n.id as news_link, n.datetime as date, 
u.name as reporter, n.content as content,p.link as pic, s.name as sport, 
s.id as sports_link, c.count as comment
from news n, pictures p, events e, sports  s, users u,
	(select news as cid,count(oid) as count
	from comments
	group by cid
	order by  count) c, 
	
	(select news as nid , pic as pid
	from news_pics
	group by news) np
where np.nid = n.id and n.id = np.nid and np.pid = p.id and c.cid= n.id and n.event = e.id and e.sport = s.id
order by comment desc
"""

select_vanues = """
select v.name as vanue, v.id as  vanue_link
from vanues v
"""

select_events = """
select e.name as event, e.id as event_link
from events e
"""
    
select_sports = """
select s.name as sport, s.id as  sport_link
from sports s
"""
    
select_countries = """
select name as country, a2_code as country_link
from countries;
"""
    
#==============================================================================
# event page
#==============================================================================
event_base = """
select e.name as event, e.date, e.time, v.name as vanue,
s.name as sport
from events e, vanues  v, sports s 
where e.vanue = v.id and e.sport = s.id and e.id =?
"""

sportsselect = "select s.name as sport, s.id as sports_link \
from sports s"
