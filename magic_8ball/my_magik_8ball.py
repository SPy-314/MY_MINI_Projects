from random import *

answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да",
           "Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы",
           "Знаки говорят - да", "Да", "Пока неясно, попробуй снова", "	Спроси позже",
           "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять",
           "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие",
           "Весьма сомнительно"]


def is_correct(correct_input):
    return correct_input in ("Да", "Нет")


print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
user_name = input("Как тебя зовут? ")
print(f"Привет {user_name}")

while True:
    question = input("Пожалуйста задай свой вопрос: ")
    print(choice(answers))
    question_2 = input("Ели хочешь еще, что-то узнать, скажи Да или Нет... ").capitalize()


    while not is_correct(question_2):
        print("Ты наверно имел ввиду Да или Нет? =) ")
        question_2 = input("Ответь просто... Да или Нет? ").capitalize()
        if question_2 == "Нет":
            print("Возвращайся если возникнут вопросы! ")
            break


    if question_2 == "Нет":
        print("Всего найлучшего! ")
        break






