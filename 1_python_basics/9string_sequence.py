# Py3 has 5 sequence types built in
# 1)The string type
# 2)list
# 3)tuple
# 4)range
# 5)bytes and bytearray


string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)

print("he's " "probably " "pining " "for the " "fjords")

print("Hello " * 5)

print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

today = "friday"
print("day" in today)  # True
print("fri" in today)  # True
print("thur" in today)  # False
print("parrot" in "fjord")  # False
