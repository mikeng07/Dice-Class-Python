import random

class Die:
    """represents a single die with 6 sides
    Attributes:
        sides(int): number of sides on die
        value (int): the value of rolled die
    """

    def __init__(self, side = 6):
        """sets the number of sides on the die with default is 6"""
        self.sides = side
        self.value = self.roll()

    def roll(self):
        """rolls the die to set the value of die. Return that value, between 1 and 6"""
        self.value = random.randint(1, self.sides)
        return self.value
    
    def __str__(self):
        """return die's value as tring"""
        return str(self.value)
    
    def __lt__(self,other):
        """return whether value of self is less than other"""
        return self.value < other.value
    
    def __eq__(self, other):
        """same but check if equal"""
        return self.value == other.value
    
    def __sub__ (self, other):
        """return the difference between value of self and other"""
        return self.value - other.value
    
    