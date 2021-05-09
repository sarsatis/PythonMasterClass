flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
]

# for flower in flowers:
#     print(flower)

# Join iterates over list
separator = ", "
output = separator.join(flowers)
print(output)

print(",".join(flowers))

####################################################################
# Join works only on string not on int
numbers = [1, 2, 3, 4, ]
print("|".join(numbers))
