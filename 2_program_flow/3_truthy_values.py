# https://docs.python.org/3/library/stdtypes.html
# In the below code 0 and '' is treated as boolean values
if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name: ")
# if name:
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")
