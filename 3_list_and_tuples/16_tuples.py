# Below is an example of tuple
t = ("a", "b", "c")
print(t)

######################################################################
# For tuples () is optional so below are few tuples with out ()
# tuples are immutable which means you cannot change the data.
# tuples saves the integrity of data hence tuples are preferred over list
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Night flight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

metallica2 = list(metallica)
print(metallica2)

metallica2[0] = "Master of Puppets"
print(metallica2)

######################################################################
# You can always unpack tuple's safely
a = b = c = d = e = f = 42
print(c)

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("Unpacking a tuple")

data = 1, 2, 76  # data represents a tuple
x, y, z = data
print(x)
print(y)
print(z)

print("Unpacking a list")

data_list = [12, 13, 14]

p, q, r = data_list
print(p)
print(q)
print(r)

######################################################################
# Enumerate returns a tuple as a return type
# In the below code index and value are unpacking tuple values
print("Enumerate tuples")
for index, value in enumerate('abcdef'):
    print(index, value)

######################################################################
# Unpack tuples using meaning ful names for better readability
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

title, artist, year = metallica
print(title)
print(artist)
print(year)

table = ("Coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2])  # In this example using index we are not sure what we are multiplying

name, length, width, height, price = table
print(length * width)
