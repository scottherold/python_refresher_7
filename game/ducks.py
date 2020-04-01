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
        aviate: overrites fly method with penguin's version of 'fly'
    """

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin a laugh? I'm a penguin!")

    def aviate(self):
        print("I won the lottery and bought a learjet")


class Mallard(Duck):
    """Example class to show why not to validate input in the Flock class""" 
    pass


class Flock(object):
    """ Class to represent a flock of birds 

    Attributes:
        flock (list[Duck]): A list of duck objects
    
    Methods:
        add_duck: add a new duck to the flock attribute
        migrate: iterates through the flock, and calls each duck's fly method
    """
    def __init__(self):
        self.flock = []

    # Python 'Hint'; this tells the programmer to only accept Duck
    # that this method only accepts Duck types, and the arrow signifies
    # that there is no return type (return type of None) for the method
    # Hints DO NOT restrict parameters of different types to be passed
    # into the method
    def add_duck(self, duck: Duck) -> None:
        # refactored to validate input argument. Is instance ensure that
        # the current instance of the argument being passed is an
        # instance of the class provided as the second argument
        # this isn't exactly 'Pythonic'
        # if isinstance(duck, Duck) is Duck:
        #     self.flock.append(duck)

        # The following method is he Pythonic way of checking if the
        # variable provided within the argument is valid. This is done
        # by checking if the object passed in has the method to be used
        # by the methods within the class (in this case fly, for
        # migrate)
        fly_method = getattr(duck, 'fly', None)
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("Cannot add duck, are you sure it's not a " + str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            # try/catch for non-ducks added to flock
            try:
                duck.fly()
                # raising errors inside your try block is a good way to
                # to check your exception handlers
                # raise AttributeError("Testing exception handler in migrate") # TODO remove this before release
            except AttributeError as e:
                print('One duck down')
                problem = e
        if problem:
            # raises the exception, so the stack trace is still
            # provided for the error. This allows the code to continue
            # executing, while still demonstrating the error
            raise problem

if __name__ == '__main__':
    donald = Duck()
    donald.fly()
