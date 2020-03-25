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
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage,
                self.hit_points))
        else:
            if self.lives > 0:
                self.lives -= 1
            else:
                print("Game Over!")

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit Points: {0.hit_points}".format(self)

# Generation of a subclass
class Troll(Enemy):
    """Subclass inherited from Enemy"""
    pass