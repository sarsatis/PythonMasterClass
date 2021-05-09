# https://docs.python.org/3/reference/expressions.html#operator-precedence
age = int(input("How old are you? "))

# if age >= 16 and age <= 65:
if 16 <= age <= 65:
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-" * 80)

# When comparing conditions using and, Python will stop checking as soon as it finds a condition that is False
# When comparing conditions using or, Python will stop checking as soon as it finds a condition that is True
if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")

day = "Friday"
temperature = 30
raining = False

if (day == "Saturday" and temperature > 27) or not raining:
    print("Go swimming")
else:
    print("Learn Python")
