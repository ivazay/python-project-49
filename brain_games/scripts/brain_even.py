from random import randint


def game_round():
    num = randint(1, 100)
    print(f'Question: {num}')
    print('Your answer: ')
    answer = input()
    correct_answer = 'yes' if num % 2 == 0 else 'no'

    if answer == correct_answer:
        return True
    else:
        print(f'"{answer}" is wrong answer ;(. '
              f'Correct answer was "{correct_answer}".')
        return False


METAINFO = {
    'round': game_round,
    'rules': 'Answer "yes" if the number is even, otherwise answer "no".'
}
