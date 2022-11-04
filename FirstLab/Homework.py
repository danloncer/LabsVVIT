#Импорт модуля math и time (чтобы программа сразу не закрывалась)
from time import *
import math as mh
#Нахождение корней квадратного уравнения (+свойста коэффициентов)
#Квадратное уравнение имеет вид:
#( ax^2 + bx + c = 0 ), где a, b, c - коэф..
#Начнем с ввода коэффициентов
print("Уравнение формы: ax^2 + bx + c = 0")
a = float(input("Введите значение коэффициента 'a':\n"))
b = float(input("Введите значение коэффициента 'b':\n"))
c = float(input("Введите значение коэффициента 'c':\n"))
#Пусть корни и дискриминант изначально будут инициализированы дефолтным значением
x1 = 0
x2 = 0
D = 0
def outPrint():
    print("Первый корень, x1 = " + str(x1))
    print("Второй корень, x2 = " + str(x2))
#После ввода пройдемся по некоторым условиям, чтобы словить одно из свойств
if (a + b + c == 0):
    x1 = 1
    x2 = c / a
    outPrint()
    sleep(30)
    exit()
elif (b == a + c):
    x1 = -1
    x2 = -c / a
    outPrint()
    sleep(30)
    exit()
elif (b % 2 == 0):
    D = (b/2)**2 - a * c
    if (D < 0):
        print("Нет корней, так как дискриминант меньше нуля")
        sleep(30)
        exit()
    if (D > 0):
        x1 = (-b / 2 + mh.sqrt(D)) / a
        x2 = (-b / 2 - mh.sqrt(D)) / a
        outPrint()
        sleep(30)
        exit()
    if (D == 0):
        x1 = (-b / 2 + mh.sqrt(D)) / a
        print("Первый корень, x1 = " + str(x1))
        sleep(30)
        exit()
else:
    D=mh.pow(b,2) - 4 * a * c
    if (D < 0):
        print("Нет корней, так как дискриминант меньше нуля")
        sleep(30)
        exit()
    if (D > 0):
        x1 = (-b + mh.sqrt(D)) / 2 * a
        x2 = (-b - mh.sqrt(D)) / 2 * a
        outPrint()
        sleep(30)
        exit()
    if (D == 0):
        x1 = (-b + mh.sqrt(D)) / 2 * a
        print("Первый корень, x1 = " + str(x1))
        sleep(30)
        exit()

