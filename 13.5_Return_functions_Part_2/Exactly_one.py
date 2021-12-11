# Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и
# возвращает значение True если слова имеют одинаковую длину и отличаются ровно в 1 символе и False в противном случае.

def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
        if count >= 2 or word1 == word2:
            return False
    return True

# вызываем функцию
print(is_one_away('aab', 'abb'))