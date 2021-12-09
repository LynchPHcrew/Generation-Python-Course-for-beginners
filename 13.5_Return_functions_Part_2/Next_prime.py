# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число большее числа num.

def get_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# считываем данные
n = int(input())


def get_next_prime(num):
    while True:
        num += 1
        if get_prime(num):
            return (num)


# вызываем функцию
print(get_next_prime(n))