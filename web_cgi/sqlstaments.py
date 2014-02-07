# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 01:37:36 2014

@author: yuankunluo
"""
#==============================================================================
# home page
#==============================================================================
lastthreeevents = """
select e.name as event, e.id as events_link,type,e.date, e.time, v.name as vanue,
s.name as sport, s.id as sports_link
from events e, vanues  v, sports s 
where e.vanue = v.id and e.sport = s.id 
order by e.date , e.time
limit 3
"""

hotnews = """
select n.title as title,n.id as news_link, n.datetime as date, 
(u.firstname ||" "||u.lastname )as reporter, n.content as content,p.link as pic, s.name as sport, 
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
select e.name as event, e.date, e.time, v.name as vanue, e.type as type,
s.name as sport, s.id as sports_link
from events e, vanues  v, sports s 
where e.vanue = v.id and e.sport = s.id and e.id =?
"""

event_results_table = """
select (a.firstname || " "||a.lastname) as athlete, a.id as athletes_link,
p.rank as rank, p.medal as medal, c.name as country
from events e, participants p, athletes a, countries c
where e.id = p.event and p.athlete = a.rowid and a.country = c.a2_code and e.id=?
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

select_all_solo_events = """
select e.name as event, e.id as events_link,e.date, e.time, v.name as vanue,
s.name as sport, s.id as sports_link
from events e, vanues  v, sports s 
where e.vanue = v.id and e.sport = s.id and e.type like "Solo%"
order by sport,date,time
"""
select_all_team_events = """
select e.name as event, e.id as events_link,e.date, e.time, v.name as vanue,
s.name as sport, s.id as sports_link
from events e, vanues  v, sports s 
where e.vanue = v.id and e.sport = s.id and e.type like "Team%"
order by sport,date,time
"""
#==============================================================================
# news page
#==============================================================================
select_all_non_event_news = """
select n.title as title, n.id as news_link, n.datetime, u.name as reporter
from news n, users u
where n.user = u.id and event = ""
order by datetime
"""
select_all_event_news = """
select n.title as title, n.id as news_link, n.datetime, u.name as reporter,e.name as event, e.id as events_link
from news n, events e, users u
where n.event = e.id and n.user = u.id
order by datetime, event
"""
#==============================================================================
# add news page
#==============================================================================
events_option = """
select (name || " -- " || type) as name, id as events_link
from events
"""
#==============================================================================
# sports page
#==============================================================================
select_all_sports = """
select s.name as sport, s.id as sports_link, c.event_count as events, s.id as sports_link
from sports s,
	(select count(e.id) as event_count, e.sport as sport
	from events e
	group by sport) c
where s.id = c.sport
"""
#==============================================================================
# athletes page
#==============================================================================
select_all_athletes = """
select (a.firstname || " " || a.lastname) as name, a.id as athletes_link, a.birthday as birthday, c.name as country
from athletes a, countries c
where a.country = c.a2_code
group by country, name
"""