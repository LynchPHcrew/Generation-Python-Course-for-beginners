# На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой.
# Напишите программу, которая определяет является ли введенная строка текста корректным ip-адресом.
adress = input().split('.')
count = 0
for i in range(len(adress)):
    adress[i] = int(adress[i])
for j in adress:
    if 0 <= j <= 255:
        count += 1
if count == 4:
    print('ДА')
else:
    print('НЕТ')