def my_func(my_list):
    for x in my_list:
        print(list(x))
        print("первое число:", x[0])
        print("последнее число:", x[-1])


my_list = [input()]
my_func(my_list)
