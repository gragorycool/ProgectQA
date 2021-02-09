def my_func(a, b):
    return list(set(a) & set(b))


import random

a = [random.randrange(0, 20) for i in range(20)]
b = [random.randrange(0, 20) for i in range(20)]
print(a)
print(b)
print("\n")

print(my_func(a, b))
