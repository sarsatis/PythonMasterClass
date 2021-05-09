print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

squares = []
for number in numbers:
    squares.append(number ** 2)

print(squares)

########################################
# Above same code can be written like below in comprehension
numbers = [1, 2, 3, 4, 5, 6]

# squares = [number ** 2 for number in numbers]
squares = [number ** 2 for number in range(1, 7)]

print(squares)


########################################
def centre_text(*args):
    # text = ""
    # for arg in args:
    #     text += str(arg) + "-"
    text = "-".join([str(arg) for arg in args])  # List comprehension
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)
centre_text("spam, spam, spam and spam")

centre_text("first", "second", 3, 4, "spam")
