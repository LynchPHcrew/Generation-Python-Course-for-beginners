s = input()
count_star = 0
count_plus = 0
for i in range(0, len(s)):
    if s[i] == '*':
        count_star += 1
    elif s[i] == '+':
        count_plus += 1
print('Cимвол + встречается', count_plus, 'раз')
print('Cимвол * встречается', count_star, 'раз')
