fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("we don't have a " + dict_key)

print(fruit)
print(fruit["lemon"])  # To access value from dictionary
print(fruit.get("lemon"))  # To access value from dictionary
fruit["pear"] = "an odd shaped apple"  # To add new value to dictionary
print(fruit)
fruit["lime"] = "great with tequila"  # To update value from dictionary
print(fruit)
del fruit["lemon"]  # Deletes a value in dictionary
fruit.clear()  # Clears all the values in dictionary
print(fruit)

######################################################################
bike = {"make": "Honda", "model": "250 dream", "colour": "red", "engine_size": 250}
print(bike["engine_size"])
print(bike["colour"])

######################################################################
# Iterating over dictionaries

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

# Dictionaries are unordered collection so 1st we order keys by using sort method once sorted we use that list to
# iterate over dictionary so that each time it provides the same o/p

# Below are some examples of doing that from less efficient way to more efficient way

ordered_keys = list(fruit.keys())
ordered_keys.sort()

ordered_keys = sorted(list(fruit.keys()))
for f in ordered_keys:
    print(f + " - " + fruit[f])

# To print keys
for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])
for f in fruit:
    print(f + " - " + fruit[f])

# To print only  values
for val in fruit.values():
    print(val)

print('-' * 40)

for key in fruit:
    print(key + "-->" + fruit[key])

fruit_keys = fruit.keys()
print(fruit_keys)

fruit["tomato"] = "not nice with ice cream"
print(fruit_keys)

#####################################################################################
# Dictionaries can be converted to list and tuples easily. And vice versa is also possible see below examples
print(fruit)
print(fruit.items())  # Creating list out of dictionary
f_tuple = tuple(fruit.items())  # Creating a tuple of list
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))  # Converting tuple back to dictionary
