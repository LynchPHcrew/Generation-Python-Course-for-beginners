# На вход программе подается натуральное число n (n≥2), а затем nn целых чисел.
# Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел.
n = int(input())
count = 0
list = []
for i in range(n):
    l = int(input())
    count += l
    list.append(count)
    count = l
print(list[1:])