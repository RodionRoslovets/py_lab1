def py_lab1():
    password = input("Введите пароль: ")
    passwordConfirm = input("Подтвердите пароль: ")

    if password == passwordConfirm:
        print("Пароль принят")
    else:
        print("Пароль не принят")