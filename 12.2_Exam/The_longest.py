#На вход программе подается строка текста.
# Напишите программу, использующую списочное выражение, которая находит длину самого длинного слова.
s = [len(i) for i in input().split()]
print(max(s))