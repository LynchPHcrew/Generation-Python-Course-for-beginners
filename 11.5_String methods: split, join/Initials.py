# На вход программе подается строка текста, содержащая имя, отчество и фамилию человека.
# Напишите программу, которая выводит инициалы человека.
s = input().split()
for i in range(len(s)):
    print(s[i][0], end = '.')