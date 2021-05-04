"""
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
чем то, что загадано. Если за 10 попыток число не отгадано, вывести правильный ответ.
"""
import random


def game(guess, answer, tries=10):
    if guess == answer:
        print('вы угадали')
        return True
    if tries <= 1:
        print(f'попытки закончились, число - {answer}')
        return False
    elif guess < answer:
        print('ваше число меньше')
    else:
        print('ваше число больше')
    guess = int(input('попробуйте еще раз:'))
    game(guess, answer, tries - 1)


user_guess = int(input('угадайте число от 0 до 100: '))
num = random.randint(0, 100)
game(user_guess, num)
