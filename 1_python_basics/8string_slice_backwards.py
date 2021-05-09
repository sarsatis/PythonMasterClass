# If you use -ve as a step value it will print backwards

letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1]  # To print a string backwards including starting value
print(backwards)

# create a slice that produces the characters qpo
print(letters[16:13:-1])

# slice the string to produce edcba
print(letters[4::-1])

# slice the string to produce the last 8 characters, in reverse order
print(letters[:-9:-1])

print(letters[-4:])
print(letters[-1:])

# Note if letters is empty string letters[0] produces error so better use idiom
letters = ""
print(letters[:1])
print(letters[0])
