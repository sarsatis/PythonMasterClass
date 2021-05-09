a = 12
b = 3

print(a + b)  # 15
print(a - b)  # 9
print(a * b)  # 36
print(a / b)  # 4.0
print(a // b)  # 4 integer division, rounded down towards minus infinity
print(a % b)  # 0 modulo: the remainder after integer division

print()

# In the below you cannot use a/b because it provides float value hence a//b is used.
for i in range(1, a // b):
    print(i)

# Operator precedence
# BODMAS = Mul & Div have equal precedence && Add and Sub have equal precedence.
# In a expression containing both div and mul or add and sub expressing is evaluated from left to right
# e.g
print(a / (b * a) / b)
