# Difference between method and function is method are inside class with self variable
# self is used to call method parameter and initialize it

class Kettle(object):
    # Class Variable
    power_source = "electricity"

    def __init__(self, make, price):
        """Below are instance variable"""
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)  # Instantiation
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))  # Calling attributes of class

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print("*" * 80)

kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power)

# Calling class variable using instances created
print("Switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print("Switch kenwood to gas")
# Assigning different power source for class variable
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)
# Below __dict_ prints all the variables and methods in the instances
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
