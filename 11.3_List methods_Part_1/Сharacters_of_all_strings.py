# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая создает список из символов всех строк, а затем выводит его.
n = int(input())
list_finish = []
for i in range(n):
    list_finish.extend(input())
print(list_finish)