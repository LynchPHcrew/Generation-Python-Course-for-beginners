# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа:
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.

def is_valid_password(password):
    password = '112:7:9'
    correct_password = password.split(':')
    for i in range(len(correct_password)):
        correct_password[i] = int(correct_password[i])
        def is_prime(n):
            count = 0
            for i in range(1, n + 1):
                if n % i == 0:
                    count += 1
            return count
    if len(correct_password) > 3:
        return False
    else:
        s = str(correct_password[0])
        n = correct_password[1]
        z = correct_password[2]
        if s == s[::-1] and is_prime(n) == 2 and z % 2 == 0:
            return True
        return False



# вызываем функцию
print(is_valid_password('112:7:9'))
