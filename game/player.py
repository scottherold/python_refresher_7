class Player(object):
    """Class to represent a basic player

    Attributes:
        name (str): The name of the player
        lives (int): The current number of lives of the player
        level (int): The current level of the player
        score (int): The current score of the player

    Methods:
        _get_lives: returns the player's current lives
        _set_lives: updates the player's current lives
        __str__: prints a string representation of the object

    Properties:
        lives: public access to lives attribute
    """
    def __init__(self, name):
        self.name = name
        self._lives = 3 # designated private attribute (hides from public)
        self.level = 1
        self.score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print('Lives cannot be negative')
            self._lives = 0

    lives = property(_get_lives, _set_lives) # public property

    # called by using the variable name for the instantiated object
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)