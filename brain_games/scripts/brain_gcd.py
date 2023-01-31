from random import randint
from math import gcd


def game_round():
    num = randint(2, 5)
    num1 = randint(1, 50) * num
    num2 = randint(1, 50) * num
    print(f'Question: {num1} {num2}')
    print('Your answer: ')
    answer = int(input())
    correct_answer = gcd(num1, num2)
    if answer == correct_answer:
        return True
    else:
        print(f'"{answer}" is wrong answer ;(. '
              f'Correct answer was "{correct_answer}".')
        return False


METAINFO = {
    'round': game_round,
    'rules': 'Find the greatest common divisor of given numbers.'
}
