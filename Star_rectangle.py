# Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14 x 10 в соответствии с образцом:
def print_pram():
    print('*' * 10, end = '')
    print()
    for i in range(1, 13):
        print('*        *')
    print('*' * 10, end = '')

print_pram()