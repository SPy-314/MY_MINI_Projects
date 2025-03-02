def caesar_cripher(text):  # Функция шифровщик по длинне слов

    res = [
        ''.join([
            chr(((ord(x) - ord('a') + sum(1 for w in word if w.isalpha())) % 26) + ord('a')) if x.islower() else
            chr(((ord(x) - ord('A') + sum(1 for w in word if w.isalpha())) % 26) + ord('A')) if x.isalpha() else x
            for x in word
        ])
        for word in text.split()
    ]

    return ' '.join(res)


user_input = input("Введите текст: ")
result = caesar_cripher(user_input)
print(result)
