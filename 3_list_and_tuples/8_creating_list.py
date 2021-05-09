#################################################################
# In the below example we will see different ways of creating list
empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits = list("432985617")
print(digits)

# Below are some ways of creating list better use copy for efficient way
# more_numbers = list(numbers)
# more_numbers = numbers[:]
more_numbers = numbers.copy()
print(more_numbers)
print(numbers is more_numbers)  # is returns if its refering to same object
print(numbers == more_numbers)  # Checks for value in list
