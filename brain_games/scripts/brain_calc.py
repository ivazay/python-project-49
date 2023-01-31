from random import randint, choice
from prompt import string
from operator import *
from functools import reduce


def welcome_user():  # repeat func
    print('Welcome to Brain Games!')
    global player_name  # bad practice
    player_name = string("What's your name? ")
    print(f'Hello, {player_name}!')


def rules():
    print('What is the result of the expression?')


def game_round():
    streak = 0
    lose = False

    while streak < 3 and lose is False:
        num1 = randint(1, 50)
        num2 = randint(1, 50)
        operators = {'+': add,
                     '-': sub,
                     '*': mul}
        operation = choice(['+', '-', '*'])

        print(f'Question: {num1} {operation} {num2}')
        print('Your answer: ')
        answer = int(input())

        correct_answer = reduce(operators[operation], [num1, num2])
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
