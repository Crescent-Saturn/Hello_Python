## Week 6 Classes and object-oriented programming
***  
###Week 6a
#### Classes
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

* All data entities in Python are objects. Compound objects consist of multiple pieces of data.
* New types of compound objects can be defined using the keyword [[class]]. For example, a class for card decks could be created using the definition statement [[class Deck]]:
* The data for objects in the class are contained in user-defined fields. For example, the Deck class could include a [[cards]] field that corresponds to a list of cards.
* Functions defined inside the class definition are methods. These method create and manipulate the object and the data in corresponding fields. For example, the Deck class might include a [[shuffle]] method that shuffles a Deck object.
 

#### Create and working with objects
* The class initializer [[__init__]]  generates instances of class objects. In Python, this initializer can be called via the expression [[class_name(...)]]. For example, an instance of the [[Deck]] class can be created via the statement [[my_deck = Deck(...)]].
* The first parameter to class methods is, by convention, always named [[self]]. This name refers to the object being acted on by the method.
* Class fields for an object are defined/modified in class methods via [[self.class_field = ...]] For example, [[self.cards = [] ]] would assign an empty list to the cards field in a class method for a Deck object.
* Class methods can be applied to a class object via [[class_object.class_method(...)]]. For example, a [[shuffle]] method could be applied to a deck via the statement [[my_deck.shuffle()]].
* Objects for user-defined classes are mutable. In particular, modification of a field in an object via a class method mutates the object.
