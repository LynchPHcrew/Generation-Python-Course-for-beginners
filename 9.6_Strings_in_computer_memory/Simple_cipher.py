# На вход программе подается строка текста.
# Напишите программу, которая переводит каждый ее символ в соответствующий ему код из таблицы символов Unicode.
s = input()
for i in s:
    print(ord(i), end = ' ')