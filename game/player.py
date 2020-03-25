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
        _get_level: return's the player's current level
        _set_level: updates the player's current level and score
        __str__: prints a string representation of the object

    Properties:
        lives: public access to lives attribute
        level: public access to level attribute
    """
    def __init__(self, name):
        self.name = name
        self._lives = 3 # designated private attribute (hides from public)
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print('Lives cannot be negative')
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print('Level cannot be less than 1')

    # public properties
    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    # public properties set using decorators
    @property
    def score(self):
        return self._score

    # syntax for setter decorator
    @score.setter
    def score(self, score):
        self._score = score

    # called by using the variable name for the instantiated object
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)