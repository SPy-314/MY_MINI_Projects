def is_correction(que, lan, step): #Функция проверки на дурака
    if que not in ('шифр', 'дешифр'):
        print('Пожалуйста запросите направление корректно')
        return False

    elif lan not in ('рус', 'анг'):
        print('Пожалуйста укажите язык правильно')
        return False

    try:
        int(step)

    except ValueError:
        print('Пожалуйста введите число корректно')
        return False

    return True


def caesar_cripher(quest, lang, key, text): #Функция шоровщик/дешифровщик
    if lang == 'анг':
        if quest == 'шифр':
            res = [
                chr(((ord(x) - ord('a') + key) % 26) + ord('a')) if x.islower() else
                chr(((ord(x) - ord('A') + key) % 26) + ord('A')) if x.isalpha() else x for x in text]
        else:
            res = [
                chr(((ord(x) - ord('a') - key) % 26) + ord('a')) if x.islower() else
                chr(((ord(x) - ord('A') - key) % 26) + ord('A')) if x.isalpha() else x for x in text]
    else:
        if quest == 'шифр':
            res = [
                chr(((ord(x) - ord('а') + key) % 32) + ord('а')) if x.islower() else
                chr(((ord(x) - ord('А') + key) % 32) + ord('А')) if x.isalpha() else x for x in text]

        else:
            res = [
                chr(((ord(x) - ord('а') - key) % 32) + ord('а')) if x.islower() else
                chr(((ord(x) - ord('А') - key) % 32) + ord('А')) if x.isalpha() else x for x in text]

    return "".join(res)


while True:
    question = input("Запросите направление (шифр/дешифр): ").lower()
    language = input("Укажите язык (рус/анг): ").lower()
    shift_step = input("Укажите шаг сдвига: ")
    if is_correction(question, language, shift_step):
        break

shift_step = int(shift_step)
user_input = input("Введите текст: ")
correction = is_correction(question, language, shift_step)
result = caesar_cripher(question, language, shift_step, user_input)
print(result)
