def py_lab2():
    placeNum = int(input('Введите номер места плацкартного вагона: '))
    result = "Тип места: "

    if placeNum < 37:
        result += "купе, "
    else:
        result += "боковое, "

    if placeNum % 2 == 0:
        result += "верхнее"
    else:
        result += "нижнее"
    
    print(result)