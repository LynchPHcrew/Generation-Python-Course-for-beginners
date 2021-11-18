# На вход программе подается натуральное число nn, а затем n различных натуральных чисел.
# Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел,
# а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.
n = int(input())
first_st = []
v = 0
for i in range(n):
    first_st.append(int(input()))
del first_st[first_st.index(max(first_st))]
del first_st[first_st.index(min(first_st))]
print(*first_st, sep = '\n')