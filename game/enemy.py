import random


class Enemy:
    """Class to represent a basic enemey to the player
    
    Attributes:
        name (str): The name of the enemy
        initial_hit_points (int): the starting hit points on an enemy
        current_hit_points (int): The current hit points of an enemy
        lives (int): The current number of lives of the enemy
        alive (boolean): Tracks if the enemy is alive (True) or dead (false)

    Methods:
        take_damage: Takes an integer as an argument (as damage). Checks to
            see if damage exceeds remaining hit points. If yes, then a life is
            removed from the lives attribute, else the hit_points attribute is
            reduced by the damage provided as an argument. If lives reduced to
            below zero, prints "Game Over"
        __str__: prints a string representation of the object
    """
    
    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.initial_hit_points = hit_points
        self.current_hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.current_hit_points - damage
        if remaining_points >= 0:
            self.current_hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage,
                self.current_hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                self.current_hit_points = self.initial_hit_points
                print("{0.name} lost a life!".format(self))
            else:
                print("{0.name} is dead!".format(self))
                self.alive = False

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit Points: {0.current_hit_points}".format(self)


# Generation of a subclass
class Troll(Enemy):
    """Subclass inherited from Enemy. Trolls have 23 hit_points.
    
    Methods:
        grunt: Prints a taunt using the troll's name
    """
    
    # example init from superclass (using super())
    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("Me {0.name}. {0.name} stromp you!".format(self))


class Vampire(Enemy):
    """Subclass inherited from Enemy. Vampires have 3 lives and 12 hit_points

    Methods:
        dodges: Generates a random number between 1 and 3. If the result is 3,
        the vampire dodges the attack.

        take_damage: overridden from the Enemy super class. Applies the dodge
        method before apply damage to the vampire hit_points
    """

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("****** {0.name} dodges ******".format(self))
            return True
        else:
            return False

    # method overriding
    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


class VampireKing(Vampire):
    """Subclass inherited from Vampire.

    Attributes:
        initial_hit_points (int): inherited from enemy super class. The 
        VampireKing subclass starts with 140 hit points.
        current_hit_points (int): inherited from enemy super class.
    
    Methods:
        take_damage: overrideen from the vampire class. Reduces damage to 1/4
        the inputted integer from the damage argument
    """

    def __init__(self, name):
        super().__init__(name=name)
        self.initial_hit_points = 140
        self.current_hit_points = 140

    # method overriding
    def take_damage(self, damage):
        super().take_damage(damage // 4)

