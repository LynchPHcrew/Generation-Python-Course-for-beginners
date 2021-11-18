# На вход программе подается натуральное число n и n строк, а затем число k.
# Напишите программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов.
# Если некоторые строки слишком короткие, и в них нет символа с заданным номером, то такие строки при выводе нужно игнорировать.
n = int(input())
ishod = []
buffer = ''
ishod2 = []
for i in range(n):
    ishod.append(input())
k = int(input())
for i in ishod:
    if k <= len(str(i)):
        buffer = i
        ishod2.append(buffer[k-1])
buffer = ''
for i in ishod2:
    buffer += i
print(buffer)