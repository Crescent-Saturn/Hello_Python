## Week 8 Notes ##
---

### Sets ###

Differences between List, Dictionary and Set:
	List -- ordered sequence  
	Dictionary -- Key-> value mapping  
	Set -- unordered collection of data with no duplicates

set(['R','W','G','Wo'])


### Collisions


d> r1 + r2 ==> No collision  
d< r1 + r2 ==> Collision


In project, we have:  
		1. Ship  
		2. rocks (set)  
		3. missiles (set)

Collision:
		ship -- rock  
		missile --rock  
	rock.collide(ship)	


def gruop_collide(g,s)  
    check each sp in g  
    does sp collide w/s ?  
    yes? remove sp from g  
return T/F  
(**Ref example_set_difference.py**)



group-group-collid(g1,g2) # g1 == rock, g2 == missile  
	group-collide()  
	
return # of collisions	
	
