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
limit 10


