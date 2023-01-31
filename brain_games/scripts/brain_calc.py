from random import randint, choice
from operator import add, sub, mul
from functools import reduce


def game_round():
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
        return True
    else:
        print(f'"{answer}" is wrong answer ;(. '
              f'Correct answer was "{correct_answer}".')
        return False


METAINFO = {
    'round': game_round,
    'rules': 'What is the result of the expression?'
}
