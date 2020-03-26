class Duck(object):
    """A class representing the animal 'duck'
    
    Methods:
        walk: prints a string representing the duck waddling
        swim: prints a string representing the duck swimming
        quack: prints a string representing the duck quacking
    """

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack quack")


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

def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()

if __name__ == '__main__':
    donald = Duck()
    test_duck(donald)

    percy = Penguin()
    test_duck(percy)