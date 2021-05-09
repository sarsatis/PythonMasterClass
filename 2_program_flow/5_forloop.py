parrot = "Norwegian Blue"

for character in parrot:
    print(character)

print("*" * 80)

number = "9,223;372:036 854,775;807"
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

print("*" * 80)

# Ranges Remember last value is not inclusive
for i in range(1, 10):
    print("i is now {}".format(i))

# Initial value can be excluded. If excluded it defaults to 0
for i in range(10):
    print("i is now {}".format(i))

# We can provide step in for loop but we have to provide initial value if we use step
for i in range(0, 10, 2):
    print("i is now {}".format(i))

for i in range(10, 0, -2):
    print("i is now {}".format(i))

print("*" * 80)

# Range can be used in if loop as well but don't prefer this
age = 5
if age in range(0, 10):
    print(age)

for i in range(1, 13):
    for j in range(1, 13):
        print("{:2} times {:2} is equal to {:3}".format(j, i, j * i))
    print("-" * 30)
