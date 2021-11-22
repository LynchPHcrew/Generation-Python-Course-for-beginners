# На вход программе подается строка текста, содержащая целые числа.
# Напишите программу, которая по заданным числам строит столбчатую диаграмму.
s = input()
numbers = s.split()
numbers2 = []
for i in range(len(numbers)):
    numbers2.append(int(numbers[i]))
for j in numbers2:
    print('+' * j, sep = '\n')