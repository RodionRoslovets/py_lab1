from tasks.py_1 import py_lab1

task = int(input("Введите номер выполняемой задачи (1 - 5): ")) 

if task == 1:
    py_lab1()
else:
    print('Неверный номер задачи')