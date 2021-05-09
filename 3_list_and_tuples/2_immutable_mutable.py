# When an object is described as immutable that means it cannot be changed
#
# Following are the immutable types built into python
#
# 1) int
# 2) float
# 3) bool
# 4) str
# 5) tuple
# 6) frozenset
# 7) bytes

result = True
another_result = result
print(id(result))
print(id(another_result))

result = False
print(id(result))

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))
print(id(another_result))


####################################################################################

# A mutable object is one whose value can be changed
#
# Python has the following mutable objects built in
# 1) list
# 2) dict
# 3) set
# 4) bytearray

shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))


# In the above example if you see in case of mutable id remains the same even after adding values to list.
# And id changes if we concatenate string this is because strings are mutable

