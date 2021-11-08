# Дано натуральное число. Напишите программу, которая вычисляет:
# количество цифр 3 в нем;
# сколько раз в нем встречается последняя цифра;
# количество четных цифр;
# сумму его цифр, больших пяти;
# произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
# сколько раз в нем встречается цифры 0 и 5 (всего суммарно).

n = int(input())
kolich_3 = 0
posled_cifr = n % 10
summ_posled_cifr = 0
chetn_chisl = 0
summa_cifr_bolshe_5 = 0
proizved_cifr_bolshe_7 = 1
kolvo_vstrech_0_and_5 = 0
while n != 0:
    if n % 10 == 3:
        kolich_3 += 1
    if posled_cifr == n % 10:
        summ_posled_cifr += 1
    if (n % 10) % 2 == 0:
        chetn_chisl += 1
    if (n % 10) > 5:
        summa_cifr_bolshe_5 += (n % 10)
    if (n % 10) > 7:
        proizved_cifr_bolshe_7 *= (n % 10)
    if ((n % 10) == 0) or ((n % 10) == 5):
        kolvo_vstrech_0_and_5 += 1
    n //= 10
print(kolich_3)
print(summ_posled_cifr)
print(chetn_chisl)
print(summa_cifr_bolshe_5)
print(proizved_cifr_bolshe_7)
print(kolvo_vstrech_0_and_5)
