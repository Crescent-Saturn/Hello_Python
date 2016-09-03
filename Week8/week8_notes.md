## Week 8 Notes ##
---

### Sets ###

Differences between List, Dictionary and Set:
	List -- ordered sequence  
	Dictionary -- Key-> value mapping  
	Set -- unordered collection of data with no duplicates

set(['R','W','G','Wo'])


**Sets** — Groups of sprites  

- Sets are unordered collections of unique objects. The initializer for Python sets is the function 𝚜𝚎𝚝().  
- Items can be added to and removed from a set using the methods 𝚊𝚍𝚍() 𝚊𝚗𝚍 𝚛𝚎𝚖𝚘𝚟𝚎(), respectively.  
- The item membership test for a set uses the keyword 𝚒𝚗.  
- The methods 𝚍𝚒𝚏𝚏𝚎𝚛𝚎𝚗𝚌𝚎() and 𝚍𝚒𝚏𝚏𝚎𝚛𝚎𝚗𝚌𝚎_𝚞𝚙𝚍𝚊𝚝𝚎() remove a set of items from a set and returns a new set or a mutated versions of the original set, respectively.  
- Lecture examples - [Sets](http://www.codeskulptor.org/#examples-sets.py), [Set differences](http://www.codeskulptor.org/#examples-set_difference.py)  
- More examples - [Set Structure](http://www.codeskulptor.org/#examples-more-8_sets-structure.py)


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


### Animation

Animation ==> continus images
**Animation** — Sprite animation

- An animated sprite is drawn by striding the center of the source rectangle in 𝚍𝚛𝚊𝚠_𝚒𝚖𝚊𝚐𝚎 through the animated sprite's associated tiled image.  
- This stride is typically controlled by the sprite's age and size.  
- This sprite's lifespan is used to terminate the animation.  
- For the Spaceship and Asteroids mini-projects, the stride is always horizontal from left to right.  
- Lecture examples - [Asteroid animation](http://www.codeskulptor.org/#examples-asteroid_animation.py), [Explosion animation](http://www.codeskulptor.org/#examples-explosion_animation.py)  
- More examples - [Running Bunny](http://www.codeskulptor.org/#examples-more-8_sprite_animation-running_bunny.py)  


**Other examples**  — [Balloon Pop (collisions)](http://www.codeskulptor.org/#examples-more-8_collisions-balloon_pop.py), [Project Template](http://www.codeskulptor.org/#examples-ricerocks_template.py)	
