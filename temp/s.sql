select cc.name as country, cc.a2_code as countries_link, cg.g as g, cs.s as s, cb.b as b,
g+s+b as summe, g*3 +s *2 + b*1 as score
from 
(select c.a2_code as a2_code, ifnull(mg.gold,0) as g
from countries c
left join (select c.a2_code as a2_code , count(cs.medal) as gold
		from 
		(select c.a2_code as country, p.team as team,
			p.medal as medal
			from countries c, athletes a, events e, participants p
			where c.a2_code = a.country and  p.event = e.id and p.athlete = a.id 
			and medal = "g"
			group by p.team
			order by c.a2_code)  cs,
			countries c
		where c.a2_code = cs.country
		group by country) mg 
		on c.a2_code= mg.a2_code) cg
		--------------------------
		,
(select c.a2_code as a2_code, ifnull(mg.gold,0) as s
from countries c
left join (select c.a2_code as a2_code , ifnull(count(cs.medal),0) as gold
		from 
		(select c.a2_code as country, p.team as team,
			p.medal as medal
			from countries c, athletes a, events e, participants p
			where c.a2_code = a.country and  p.event = e.id and p.athlete = a.id 
			and medal = "s"
			group by p.team
			order by c.a2_code)  cs,
			countries c
		where c.a2_code = cs.country
		group by country) mg 
		on c.a2_code= mg.a2_code) cs
		------------------------------
		,
		(select c.a2_code as a2_code, ifnull(mg.gold,0) as b
from countries c
left join (select c.a2_code as a2_code , count(cs.medal) as gold
		from 
		(select c.a2_code as country, p.team as team,
			p.medal as medal
			from countries c, athletes a, events e, participants p
			where c.a2_code = a.country and  p.event = e.id and p.athlete = a.id 
			and medal = "b"
			group by p.team
			order by c.a2_code)  cs,
			countries c
		where c.a2_code = cs.country
		group by country) mg 
		on c.a2_code= mg.a2_code) cb,
		countries cc
where cc.a2_code = cb.a2_code and cb.a2_code = cs.a2_code and cs.a2_code = cg.a2_code

