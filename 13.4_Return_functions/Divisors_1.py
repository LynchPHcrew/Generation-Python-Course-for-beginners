# Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце.

def get_factors(num):
    return [n for n in range(1, num + 1) if num % n == 0]

print(get_factors(1))
print(get_factors(5))
print(get_factors(10))