# Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце.

def get_days(month):
    if month == 2:
        return 28
    if month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

print(get_days(1))
print(get_days(2))
print(get_days(10))