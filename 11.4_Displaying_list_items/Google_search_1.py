# На вход программе подается натуральное число n, затем nn строк, затем еще одна строка — поисковый запрос.
# Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.
n = int(input())
set = []
set2 = []
for i in range(n):
    set.append(input())
zapros = input()
for x in set:
    if zapros.lower() in x.lower():
        set2.append(x)
print(*set2, sep = '\n')