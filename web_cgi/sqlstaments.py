# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 01:37:36 2014

@author: yuankunluo
"""
#==============================================================================
# home page
#==============================================================================
lastthreeevents = """
select e.name as event, e.id as events_link,e.date, e.time, v.name as vanue,
s.name as sport, s.id as sports_link
from events e, vanues  v, sports s 
where e.vanue = v.id and e.sport = s.id 
order by e.date , e.time
limit 3
"""

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
event_page_eventinfo = """
select e.name as event, e.date, e.time, v.name as vanue,
s.name as sport, s.id as sports_link
from events e, vanues  v, sports s 
where e.vanue = v.id and e.sport = s.id and e.id =?
"""

event_results_table = """
select (a.firstname || " "||a.lastname) as athlete, a.rowid as athletes_link,
p.rank as rank, p.medal as medal
from events e, participants p, athletes a
where e.id = p.event and p.athlete = a.rowid and e.id=?
order by rank
"""

event_news_table = """
select n.title as title, n.id as news_link, u.name as reporter 
from news n,  events e, users u
where n.event = e.id and e.id = ?
"""

select_all_events = """
select e.name as event, e.id as events_link,e.date, e.time, v.name as vanue,
s.name as sport, s.id as sports_link
from events e, vanues  v, sports s 
where e.vanue = v.id and e.sport = s.id
order by sport,date,time
"""

#==============================================================================
# news page
#==============================================================================
select_all_news = """
select n.title as title, n.id as news_link, n.datetime, u.name as reporter,e.name as event, e.id as events_link
from news n, events e, users u
where n.event = e.id and n.user = u.id
order by datetime, event
"""