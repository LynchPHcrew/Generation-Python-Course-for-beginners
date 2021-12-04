# Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце.

def number_of_factors(num):
    return len([n for n in range(1, num + 1) if num % n == 0])

print(number_of_factors(1))
print(number_of_factors(5))
print(number_of_factors(10))