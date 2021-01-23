def my_func():
    a = int(input("Введите год:"))
    if a % 4 != 0:
        print("Обычный")
    elif a % 100 == 0:
        if a % 400 == 0:
            print("Високосный")
        else:
            print("Обычный")
    else:
        print("Високосный")

my_func()
