# Class creation
class Kettle(object):

    # __init__ is the constructor
    # self is a reference to the INSTANCE of the class
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


# instance of class
kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, 
    hamilton.make, hamilton.price))

# With OOP you can specify attributes in the replacement fields
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood,
    hamilton))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics
Object: an instance of a class.
Instantiate: creae an intance of a class.
Method: a function defined in a class. Single blank lines for methods, instead of hte two for functions
Attribute: a variable bound to an instance of a class.
"""

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

# You can call a methof from the actual class, but you must pass in an
# object of that class type to satisfy the 'self' parameter
Kettle.switch_on(kenwood)
print(kenwood.on)

print("*" * 80)

# like everything in Python, classes are dynamic. This means, you can
# modify classes after creation/instansiation

# new attribute power
kenwood.power = 1.5
print(kenwood.power)