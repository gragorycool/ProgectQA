def my_func():
    a = int(input("Введите число:"))
    print("Сумма цифр: ", sum(int(x) for x in str(a)))


my_func()
