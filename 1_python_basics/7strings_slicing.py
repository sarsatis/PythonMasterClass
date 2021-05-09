# Slicing with +ve values

#                   1
#         012345678901234
parrot = "Norwegian Blue"

print(parrot[0:6])  # Norweg
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])  # Omits the start of the string

print(parrot[10:14])
print(parrot[10:])  # Omits the end of the string

print(parrot[:])  # Omits both start & end of the string to provide complete string

# Slicing with -ve values
#                   1
#         012345678901234
parrot = "Norwegian Blue"

print(parrot[0:6])  # Norweg
print(parrot[-14:-8])  # Norweg

print(parrot[-4:-2])  # Bl
print(parrot[-4:12])  # Bl

# Note
# This is not possible because when using -ve indexing end index should be value ahead of it not behind it.
# It will not give any error but it will not print anything
print(parrot[-4:2])

# Slicing using step
#                   1
#         012345678901234
parrot = "Norwegian Blue"

print(parrot[0:6:2])  # Nre  here step used is 2
print(parrot[0:6:3])  # Nw   here step used is 3

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
