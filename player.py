import die

class Player:
    """
    represent a player of dice game where they roll a set of 3 dice
    to see if they get a pair, series or 3 of a kind
    attributes: 
        dice(list of die object)
        points: player points
    """

    def __init__(self):
        """Initialize list of dice and points"""
        self.dice = [die.Die(),die.Die(),die.Die()]
        self.dice.sort()
        self.points = 0

    def get_points(self):
        """return player's point"""
        return self.points  
    
    def roll_dice(self):
        """roll player dice and sort them"""
        for d in self.dice:
            d.roll()
        self.dice.sort()

    def has_pair(self):
        """
        return true if 2 dice in the list has same value
        """
        if self.dice[0] == self.dice[1] or  self.dice[1] == self.dice[2] or  self.dice[0] == self.dice[2]:
            self.points += 1
            return True
        return False  
    
    def has_three_of_a_kind(self):
        """
        return true if 3 dice has same value
        """
        if  self.dice[0] == self.dice[1] == self.dice[2]:
            self.points += 3
            return True
        return False
    
    def has_series(self):
        """
        return true if the value of dice is in a sequences
        """
        if self.dice[1] - self.dice[0] == 1 and self.dice[2] - self.dice[1] == 1:
            self.points += 2
            return True
        return False
    def __str__(self):
        """return string representation of 3 dice"""
        return "D1=" + str(self.dice[0]) + " D2=" + str(self.dice[1]) + " D2=" + str(self.dice[2])
    


        