print("Today is a good day to learn Python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")
greeting = "Hello"
name = input("Please enter your name ")
print(greeting + name)

# if we want a space, we can add that too
print(greeting + ' ' + name)

print(type(greeting))

# In python variable can be reused. for eg below age is first saved as int and then again assigned as string
age = 24
print(age)

age = "2 years"
print(age)

# In python cannot concatenate str and int
age = 24
name = "sar"
print(name + age)
