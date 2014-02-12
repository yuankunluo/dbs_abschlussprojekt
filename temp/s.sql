select *
from countries 
	-- mg
	(select c.a2_code as a2_code , count(cs.medal) as gold
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
	
	-- ms
	(select c.a2_code as a2_code , count(cs.medal) as silber
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
		group by country)  ms
		
		-- mb
(select c.a2_code as a2_code , count(cs.medal) as brozen
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
		group by country) as mb
--------------


-------------------------------------------------------------------------
select cc.name as name, cg.g as g, cs.s as s, cb.b as b
from 
(select c.a2_code as a2_code, mg.gold as g
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
(select c.a2_code as a2_code, mg.gold as s
from countries c
left join (select c.a2_code as a2_code , count(cs.medal) as gold
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
		(select c.a2_code as a2_code, mg.gold as b
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
