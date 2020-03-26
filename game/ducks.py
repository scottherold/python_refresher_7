class Wing(object):
    """A class reprensenting a bird's wing

    Attributes:
        ratio (float): The ratio of wing size, to bird body

    Methods:
        fly: determines if the ratio is large enough for a bird to fly
    """

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Wee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):
    """A class representing the animal 'duck'

    Attributes:
        wing (Wing): 
    
    Methods:
        walk: prints a string representing the duck waddling
        swim: prints a string representing the duck swimming
        quack: prints a string representing the duck quacking
        fly: composed method from the Wing class
    """

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):
    """A class representing the animal 'penguin'
    
    Methods:
        walk: prints a string representing the penguin waddling
        swim: prints a string representing the penguin swimming
        quack: prints a string representing the penguin quacking
    """

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin a laugh? I'm a penguin!")

# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()

if __name__ == '__main__':
    donald = Duck()
    donald.fly()

    # percy = Penguin()