shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# Continue ignores/skips the current values and continues until end of list

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        continue

    print("Buy " + item)

# Note if we dont add break it will search for all the items in the list even if the item is found at index 3
item_to_be_found = "spam"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_be_found:
        found_at = index
        break

if found_at is not None:
    print("{} found at {}".format(item_to_be_found, found_at))
else:
    print("{} item not found".format(item_to_be_found))

# Above break code can also be written as below. Use below approach since python is a rich language use built in functions
item_to_be_found = "alberto"
found_at = None

if item_to_be_found in shopping_list:
    found_at = shopping_list.index(item_to_be_found)

if found_at is not None:
    print("{} found at {}".format(item_to_be_found, found_at))
else:
    print("{} item not found".format(item_to_be_found))
