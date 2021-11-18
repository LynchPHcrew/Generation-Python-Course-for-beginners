# На вход программе подается натуральное число nn, а затем n целых чисел.
# Напишите программу, которая для каждого введенного числа x выводит значение функции f(x) = x^2 + 2x + 1, каждое на отдельной строке.
n = int(input())
first = []
second = []
for num in range(n):
    num = int(input())
    first.append(num)
    second.append(num**2 + 2*num + 1)
print(*first, sep='\n')
print()
print(*second, sep='\n')
