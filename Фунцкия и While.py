def my_function():
    print("Подсчет закончен.")

a = 7
b = 20
v = 3
while a < b:
    print(a, "Пока что нет.")
    a += v

else:
    print("\n" + "Дождались!:", int(a))

my_function()
