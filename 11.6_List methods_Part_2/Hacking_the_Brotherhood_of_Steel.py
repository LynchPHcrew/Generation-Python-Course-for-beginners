# Известно, что программисты Братства никогда не оставляют комментарии к коду, и пишут программы на Python, поэтому удаление всех этих комментариев никак не навредит им.
# Помогите писцу Ибсену удалить все комментарии из программы.

# На первой строке вводится символ решётки и сразу же натуральное число n — количество строк в программе, не считая первой.
# Далее следует n строк кода.
s = input()
n = s[1:]
for i in range(int(n)):
    string = input()
    for j in string:
        if '#' in string:
            break
    print(string.split('#')[0].rstrip())