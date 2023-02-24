from tasks.py_1 import py_lab1
from tasks.py_2 import py_lab2
from tasks.py_3 import py_lab3

task = int(input("Введите номер выполняемой задачи (1 - 5): ")) 

if task == 1:
    py_lab1()
elif task == 2:
    py_lab2()
elif task == 3:
    py_lab3()
else:
    print('Неверный номер задачи')