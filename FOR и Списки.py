import random

a = [random.randrange(0, 9) for x in range(15)]
print(a)
print("размер списка:", len(a), "элементов")
search = input("введите число для поиска:")
b = [i for i, x in enumerate(a) if x == 7]
if b == ([]):
    print("\n")
    print("такого числа нет в списке")
else:
    print("id:", b, "цыфра", 7)



