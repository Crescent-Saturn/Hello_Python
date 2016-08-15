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

=======
**Remember to call class methods via object_name.method(...)**

**Remember that an object is created via class_obj = ClassName(...)**  
The self paramter is created by Python.  

*Quitz: If particel is a Python list, what will happen if you execute the following line of Python in the draw handler:`particle.draw(canvas)`*  
>Solution: you will get an AttributeError because list does not have a draw method.


* The class initializer [[__init__]]  generates instances of class objects. In Python, this initializer can be called via the expression [[class_name(...)]]. For example, an instance of the [[Deck]] class can be created via the statement [[my_deck = Deck(...)]].
* The first parameter to class methods is, by convention, always named [[self]]. This name refers to the object being acted on by the method.
* Class fields for an object are defined/modified in class methods via [[self.class_field = ...]] For example, [[self.cards = [] ]] would assign an empty list to the cards field in a class method for a Deck object.
* Class methods can be applied to a class object via [[class_object.class_method(...)]]. For example, a [[shuffle]] method could be applied to a deck via the statement [[my_deck.shuffle()]].
* Objects for user-defined classes are mutable. In particular, modification of a field in an object via a class method mutates the object.

=======


#### Classes for Blackjack
**Blackjack**:
* Card -- rank & suit (image)
* Hand -- collection of cards [hit score]
* Deck -- collection of cards [shuffle deal]

*Quitz: Why should a blackjack hand and a deck of cards be implemented as two different classes?*  
>Solution: They each have different behaviors and you might reuse the deck class in a different card game. The hand is specific to blackjack.  



###Week 6b
#### Tired Images
* A tiled image is a single image that consists of a set of smaller images laid out in a regular grid.
* Tiled images are useful since loading a single large image is faster than loading many small images.
* Small images in the tiled image can be drawn by specifying the appropriate source rectangle for 𝚍𝚛𝚊𝚠_𝚒𝚖𝚊𝚐𝚎 using the size of the small image and its position in the grid.
* Lecture examples - [Tiled Images](http://www.codeskulptor.org/#examples-tiled_images.py)
* More examples - [Bunny Emotions](http://www.codeskulptor.org/#examples-more-6_tiled_images-bunny_emotions.py)


*Quitz: What information do you need to draw a single image from a tiled image?*
> Solution: The size (width and height) of each image and how the images are arranged in the tiled image.  


#### Programming tips

**Ref:programming-tips-6.py**

<<<<<<< HEAD
=======
===

### Mini-project Notes

#### Blackjack

**Determining  the value of a hand**    
> Value of a card  
> * Nb card == Nb  
> * J,Q,K == 10  
> * Ace == 1 or 11 (player's choice)  

> Value of Blackjack hand  
> * Key: **Nevers count 2 Aces as 11**  
> * hand_value = sum(cards_value with Aces as 1)  
> * If the hand has no Aces:  
>   return hand_value  
> * elif hand_value +10 <= 21:  
>   return hand_value + 10  
> * else  return hand_value  

**Determining when the dealer should stand**

> While the value of the dealer's hand is less than 17  
> * hit the dealer'hand


Python- while loop
```
while test:  
    body
```

Use the get_value method for a hand inside test  
Use the hit method for hand inside the body  



>>>>>>> dev
