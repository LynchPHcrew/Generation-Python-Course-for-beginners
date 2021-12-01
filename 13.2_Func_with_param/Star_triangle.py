# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
#
# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;
# а затем выводит его:

def draw_triangle(fill, base):
    for i in range(1, base // 2 + 2):
        print(fill * i, end='\n')
    for j in range(base // 2):
        print(fill * ((base // 2) - j), end='\n')

draw_triangle('*', 9)
