
from random import *

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_."
no_punctuation = "il1Lo0O"

#Да это функция all и генераторы.. я до этого курса, еще курсы проходил, так что извините....
def is_correction(*args):
    x = all(arg.isdigit() for arg in args[:2])
    y = all(arg == "yes" or arg == "no" for arg in args[2:])
    return x and y


def generate_password(leng, quan, string_chars, no_punct):
    lst_password = []
    for _ in range(int(quan)):
        if no_pun_cse == "yes":
            chrs = "".join(char for char in string_chars if char not in no_punct)

        password = "".join(choice(string_chars) for _ in range(int(leng)))
        lst_password.append(password)

    return lst_password


while True:
    quan_password = input("Задайте кал-во паролей (введите число): ")
    len_password = input("Задайте длинну (введите число): ")
    dig_cse = input(f"Включать ли цифры {digits}? (yes/no): ").lower()
    up_cse = input(f"Включать ли строчные буквы {lowercase_letters}? (yes/no): ").lower()
    low_cse = input(f"Включать ли заглавные буквы {uppercase_letters}? (yes/no): ").lower()
    pun_cse = input(f"Включать ли символы {punctuation}? (yes/no): ").lower()
    no_pun_cse = input(f"Исключать ли неоднозначные символы {no_punctuation}? (yes/no): ").lower()

    if is_correction(quan_password, len_password, dig_cse, up_cse, low_cse, pun_cse, no_pun_cse):
        chars = ""
        chars += digits if dig_cse == "yes" else ""
        chars += lowercase_letters if low_cse == "yes" else ""
        chars += uppercase_letters if up_cse == "yes" else ""
        chars += punctuation if pun_cse == "yes" else ""
        break

    else:
        print("Пожалуйста корректно введите данные...")
        continue

my_passwords = generate_password(len_password, quan_password, chars, no_pun_cse)
print('\nВот список паролей: ')
print(*my_passwords, sep="\n")
