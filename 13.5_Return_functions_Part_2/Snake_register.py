# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».

# объявление функции
def convert_to_python_case(text):
    s = text[0].lower()
    for i in text[1:]:
        if i != i.lower():
            s += '_' + i.lower()
        else:
            s += i
    return s


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))