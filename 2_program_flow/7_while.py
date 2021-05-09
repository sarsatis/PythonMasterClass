i = 0
while i < 10:
    print(i)
    i += 1

print("-" * 80)

# Note while loops evaluates only on true conditions

available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break

print("aren't you glad you got out of there")
