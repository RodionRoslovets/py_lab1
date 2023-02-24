def py_lab4():
    acceptedColors = ["красный", "желтый", "синий"]
    purple = ["красный", "синий"]
    orange = ["красный", "желтый"]
    green = ["желтый", "синий"]

    firstColor = input('Введите первый цвет: ').lower() 
    secondColor = input('Введите второй цвет: ').lower() 

    if firstColor in acceptedColors and secondColor in acceptedColors:
        if firstColor == secondColor:
            print('Введены одинаковые цвета')
            return

        if firstColor in purple and secondColor in purple:
            print('Фиолетовый')
            return
        if firstColor in orange and secondColor in orange:
            print('Оранжевый')
            return
        if firstColor in green and secondColor in green:
            print('Зеленый')
            return
    else:
        print('Введено неверное название цвета')