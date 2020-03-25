class Enemy:
    """Class to represent a basic enemey to the player
    
    Attributes:
        name (str): The name of the enemy
        hit_points (int): The current hit points of an enemy
        lives (int): The current number of lives of the enemy

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
    """

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)