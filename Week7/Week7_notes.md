### Week 7 Physic controls
---
#### 7a  **Acceleration control**--Acceleration and Friction

* Basic physics relates the position of a point p, its velocity vector v and its acceleration vector a via the update equations 
p=p+v∗dt
v=v+a∗dt
* In the absence of friction, the acceleration vector for the Asteroids ship is a scaled version of the forward vector f where f=(cos(θ),sin(θ)). Here, θ is the angle with the horizontal axis.
* Application of acceleration using the forward thrust vector is controlled using keyboard input.
* To add friction to this model, the velocity of the ship is continually decelerated via the update v=e∗v where e is a constant slightly smaller than 1.

**Sound** — Sound

* The SimplGui function 𝚕𝚘𝚊𝚍_𝚜𝚘𝚞𝚗𝚍() loads a sound file, specified as a URL, into CodeSkulptor and returns a sound object.
* The method 𝚜𝚎𝚝_𝚟𝚘𝚕𝚞𝚖𝚎() controls the playback volume of the sound.
* The methods 𝚙𝚕𝚊𝚢(),𝚙𝚊𝚞𝚜𝚎(),𝚛𝚎𝚠𝚒𝚗𝚍() control the playback of the sound object.
* Attempting to play several versions of the same sound object at the same time in not possible. However, different sounds objects can play on different channels simultaneously.
* Different browser support different sound formats. Short sounds are laggy in Firefox.
* Lecture examples - [Sound](http://www.codeskulptor.org/#examples-sound.py)
* More examples - Bouncing Ball


##### 7b  **Sprites** — Sprite class

* Most object-oriented game environments provide a class structure for 2D graphical/image objects called sprites.
* The Sprite class typically includes fields for quantities such as position, velocity, size and age.
* This class typically includes an initializer, an update method, a draw method and a collision method.
* For the Spaceship and Asteroids mini-projects, sprites have an associated 𝙸𝚖𝚊𝚐𝚎𝙸𝚗𝚏𝚘 class with fields that contain the center, size, radius, lifespan and animated flag for an image.
* Lecture examples - [Sprite Example](http://www.codeskulptor.org/#examples-sprite_example.py), [Spaceship](http://www.codeskulptor.org/#examples-spaceship.py), [Project Template](http://www.codeskulptor.org/#examples-spaceship_template.py)
* More examples - [Curling](http://www.codeskulptor.org/#examples-more-7_acceleration_and_friction-curling.py)
