import exit_module


def phone_book():
    print("Меню:")
    print("1. Создать Контакт")
    print("2. Найти Контакт")
    print("3. Отредактировать Контакт")
    print("4. Удалить Контакт")
    print("5. Выйти")

    a = int(input("Выбери действие: "))

    if a == 1:
        print("Действие не назначенно!")
    elif a == 2:
        print("Действие не назначенно!")
    elif a == 3:
        print("Действие не назначенно!")
    elif a == 4:
        print("Действие не назначенно!")
    elif a == 5:
        exit_module.exit_module()

    else:
        print("Не Существующее действие!")

    phone_book()
    a = int(input("Выбери действие: "))


phone_book()
