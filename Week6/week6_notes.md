### Week 6 Classes and object-oriented programming
***  
Week 6a - Classes
定义：
```python
class Character:
    def __init__(self, name, initial_health):
        self.name = name
        self.health = initial_health
        self.inventory = []
        
```
*Quitz: How to create an object of type [[Rice]] and assign it to the variable owls?*
> Solution:
`owls = Rice("hot")`

*Quitz2: What code would you need to write in order to extend the example of this lecture (ref example-oo-ball.py) so that the ball would bounce around inside an oval?*  
>Solution:  
You would need to write a class [[OvalDomain]] with the same methods as [[RectangularDomain]] and create an object of type [[OvalDomain]] to pass the ball as its domain.

