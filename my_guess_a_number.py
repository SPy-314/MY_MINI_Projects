from random import *


def is_correct_input(correct_input):
    return correct_input in ("Да", "Нет")


def is_valid(number, left, right):
    return left <= number <= right


print('Добро пожаловать в числовую угадайку!')
user_input = input("Хотите ли вы играть? (введите Да или Нет): ").capitalize()
while user_input != "Нет":
    count = 0
    if not is_correct_input(user_input):
        print('Введите ответ Да или Нет')
        user_input = input("Хотите ли вы играть? (введите Да или Нет): ").capitalize()
        continue

    else:
        left, right = 1, int(input("Введите правую границу числа: "))
        guess_a_number = randint(left, right)
        while True:
            num = int(input(f"Введите число от {left} до {right}: "))
            if not is_valid(num, left, right):
                print(f'А может быть все-таки введем целое число от {left} до {right}?')
                continue

            else:
                count += 1
                if num > guess_a_number:
                    print('Ваше число больше загаданного, попробуйте еще разок')
                    continue
                elif num < guess_a_number:
                    print('Ваше число меньше загаданного, попробуйте еще разок')
                    continue
                else:
                    print('Вы угадали, поздравляем!')
                    print(f"Вы угадали с {count} попытки =)")
                    break


    user_input = input("Хотите сыграть снова? (введите Да или Нет): ").capitalize()

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

