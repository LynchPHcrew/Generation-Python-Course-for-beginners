s = input()
count_vowels = 0
count_consonants = 0
for i in range(0, len(s)):
    if s[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        count_vowels += 1
    elif s[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        count_consonants += 1
print('Количество гласных букв равно', count_vowels)
print('Количество cогласных букв равно', count_consonants)
