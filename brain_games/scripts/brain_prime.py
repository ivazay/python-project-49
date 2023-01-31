from random import randint


def is_prime(n: int) -> bool:
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def game_round():
    num = randint(3, 50)
    print(f'Question: {num}')
    print('Your answer: ')
    answer = input()
    correct_answer = 'yes' if is_prime(num) else 'no'

    if answer == correct_answer:
        return True
    else:
        print(f'"{answer}" is wrong answer ;(. '
              f'Correct answer was "{correct_answer}".')
        return False


METAINFO = {
    'round': game_round,
    'rules': 'Answer "yes" if the number is prime, otherwise answer "no".'
}
