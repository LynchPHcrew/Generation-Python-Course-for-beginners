# На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов,
# затем k строк — поисковые запросы.
# Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.
n = int(input())
set1 = []
set2 = []
set3 = []
count = 0
for i in range(n):
    set1.append(input())
k = int(input())
for j in range(k):
    set2.append(input())
for i in set1:
    count = 0
    for j in set2:
        if j.lower() in i.lower():
            count += 1
            if count == len(set2):
                set3.append(i)
                count = 0
print(*set3, sep = '\n')