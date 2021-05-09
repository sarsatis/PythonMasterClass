mylist = [['abc'], ['def', 'ghi']]
print(mylist[-1][-1][-1])

x = 10.0

if type(x) == float:
    print(int(x))
else:
    print(x)

price = 10 * 2.5
print(price)

x = [len(item) for item in ['abc', 'def', 'ghi']]
print(x)

y = [i * 2 if i > 0 else 0 for i in [1, -2, 10]]
print(y)

def foo(*args):
    return len(args)
print(foo(1, 2, 4))

def foo(x):
    return x ** 2
print(foo("Hello"))