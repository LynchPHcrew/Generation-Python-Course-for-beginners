# На вход программе подается натуральное число, записанное в десятичной системе счисления. Напишите программу, которая переводит данное число в двоичную систему счисления.
s = int(input())
total = ''
b = 0
while s != 0:
    b += s % 2
    total = str(b) + total
    s //= 2
    b = 0
print(total)
