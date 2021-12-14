# Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, состоящую из символов ( и ) и возвращает значение True если поступившая на вход строка является правильной скобочной последовательностью и False в противном случае.

def is_correct_bracket(text):
    count = 0
    if text.startswith(')') or text.endswith('('):
        return False
    for c in text:
        if c == '(':
            count += 1
        if c == ')':
            if count == 0:
                return False
            else:
                count -= 1
    if count == 0:
        return True
    return False


# вызываем функцию
print(is_correct_bracket('())()()()('))
