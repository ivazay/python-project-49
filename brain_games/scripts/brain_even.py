from random import randint
from prompt import string


def welcome_user():
    print('Welcome to Brain Games!')
    global player_name
    player_name = string("What's your name? ")
    print(f'Hello, {player_name}!')


def rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def game_round():
    streak = 0
    lose = False

    while streak < 3 and lose is False:
        num = randint(1, 100)
        print(f'Question: {num}')
        print('Your answer: ')
        answer = input()
        correct_answer = 'yes' if num % 2 == 0 else 'no'

        if answer == correct_answer:
            print('Correct!')
            streak += 1
        else:
            lose = True
            print(f'"{answer}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}".')
            print(f"Let's try again, {player_name}!")

    if streak == 3:
        print(f'Congrats, {player_name}!')


def run_game():
    welcome_user()
    rules()
    game_round()
