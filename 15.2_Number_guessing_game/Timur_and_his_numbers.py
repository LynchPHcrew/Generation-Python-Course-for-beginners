import random                    # подключаем модуль
number = random.randint(1, 101)  # генерируем случайное число от 1 до 100
print('Добро пожаловать в числовую угадайку')
def is_valid(num):
    if num.isdigit():
        num = int(num)
        if 1 <= num <= 100:
            return True
        else:
            return False
    else:
        return False
import random                    # подключаем модуль

number = random.randint(1, 101)  # генерируем случайное число от 1 до 100

print('Добро пожаловать в числовую угадайку')

while True:
    response = input('Введите число от 1 до 100:')
    if not is_valid(responce):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    response = int(response)
import random  # подключаем модуль

number = random.randint(1, 101)  # генерируем случайное число от 1 до 100

print('Добро пожаловать в числовую угадайку')

while True:
    response = input('Введите число от 1 до 100:')
    if not is_valid(responce):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    response = int(response)

    if val < number:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif val > number:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
