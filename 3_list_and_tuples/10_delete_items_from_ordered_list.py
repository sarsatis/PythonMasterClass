data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

# del data[0:2]
# print(data)
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200

# Always remember deleting data will reduce the size of list so index value will not work appropriately
# for example in the below for loop it will not remove 5 and 360 because once we delete 4 and 350 index value
# of list will change
# when deleting values from list its always better to run loop in reverse hint: see 11_delete_items_from_unordered_list
for index, value in enumerate(data):
    if (value < min_valid) or (value > max_valid):
        del data[index]

print(data)

# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)  # for debugging
del data[:stop]
print(data)

# process the high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        # We have the index of the last item to keep.
        # Set 'start' to the position of the first
        # item to delete, which is 1 after 'index'.
        start = index + 1
        break

print(start)  # for debugging
del data[start:]
print(data)
