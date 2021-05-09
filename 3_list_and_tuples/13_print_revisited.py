# Print function can take arguments e.g print(*objects,sep=",",end="\n")

name = "Tim"
age = 10

print(name, age, "Python", 2020)
print(name, age, "Python", 2020, sep=", ")

########################################################################################

menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=", ")
    print()

########################################################################################
# The above code print , at the end of the o/p to ignore that we use python generators
print()
for meal in menu:
    items = ", ".join((item for item in meal if item != "spam"))
    print(items)

