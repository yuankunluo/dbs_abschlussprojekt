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
select n.name as title,n.id as news_link, n.datetime as date, 
u.name as reporter, n.content as content,p.link as pic, s.name as sport, 
s.id as sports_link, c.count as comment
from news n, pictures p, events e, sports s, users u,
	(select news as nid,count(oid) as count
	from comments
	group by nid
	order by  count) c, 
	(select ns.news as npnid , ns.pic as pid
	from newspics ns
	group by news) np
where np.npnid = n.id and np.pid = p.id and c.nid= n.id and n.event = e.id and e.sport = s.id 
group by news_link
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
select n.name as title, n.id as news_link, u.name as reporter 
from news n,  events e, users u
where n.event = e.id and e.id = ?
group by news_link
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
select n.name as title, n.id as news_link, n.datetime, u.name as reporter
from news n, users u
where n.user = u.id and event = ""
order by datetime
"""
select_all_event_news = """
select n.name as title, n.id as news_link, n.datetime, u.name as reporter,e.name as event, e.id as events_link
from news n, events e, users u
where n.event = e.id and n.user = u.id
order by datetime, event
"""
select_one_news = """
select n.id as id, u.name as reporter, n.datetime as datetime, n.content as content, n.name as name
from news n, users u
where n.user = u.id and n.id = ?
"""
select_news_pics = """
select  p.link, p.des, u.name
from news n, newspics np, pictures p, users u
where n.id = np.news and np.pic = p.id and np.user = u.id and n.id = ?
"""
select_news_event = """
select e.name as event,e.id as events_link, e.date, e.time, v.name as vanue, e.type as type,
s.name as sport, s.id as sports_link
from events e, vanues  v, sports s , news n
where e.vanue = v.id and e.sport = s.id and e.id = n.event and n.id = ?
"""
select_news_comment = """
select u.name as name, p.link as pic, c.datetime as datetime, c.content as comment, p.des as picdes
from comments c, users u, pictures p, news n
where c.user = u.id and u.pic = p.id and c.news = n.id and n.id = ?
order by datetime desc
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

select_one_ath = """
select a.id as id, (a.firstname ||" "|| a.lastname) as name, a.firstname as firstname,  a.lastname as lastname,
 a.gender as gender,  a.birthday as birthday, c.name as country, p.link as pic
from athletes a, countries c, pictures p
where a.country = c.a2_code and a.pic = p.id and a.id = ?
"""

ath_medals = """
select e.name as event, e.id as events_link, e.type as type, p.medal as medal, p.result as result
from events e, participants p, athletes a
where p.event = e.id and p.athlete = a.id and a.id = ? and p.medal IN ("g","s","b") 
order by p.rank
"""

ath_others = """
select e.name as event, e.id as events_link,  e.type as type, e.date as date, 
p.rank as rank, p.result as result,s.name as sport , s.id as sports_link
from events e, participants p, athletes a, sports s
where p.event = e.id and p.athlete = a.id and p.medal NOT IN ("g","s","b") and e.sport = s.id and a.id = ?
order by p.rank
"""

ath_news = """
select n.name as title, n.id as news_link, n.datetime as datetime
from events e, participants p, athletes a, news  n
where e.id = p.event and p.athlete = a.id and n.event = e.id and a.id = ?
order by datetime
"""
#==============================================================================
# admin page
#==============================================================================
a_options = """
select (a.firstname || " " || a.lastname || " -- " || c.name) as name, a.id as athletes_link
from athletes a, countries c
where a.country = c.a2_code
order by  c.name, a.firstname, a.lastname
"""

n_options = """
select (n.name || " -- " || date(n.datetime) )as title, n.id as news_link
from news  n
order by n.datetime
"""

select_one_user = """
   select u.id as id, u.name as name, u.email as email, u.firstname as firstname, 
   u.lastname as lastname, u.gender as gender, u.birthday as birthday, 
   c.name as country, p.link as pic, p.des as picdes
   from users u, pictures p, countries c
   where u.pic = p.id and  c.a2_code = u.country and u.id = ?
"""