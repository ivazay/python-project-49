from random import randint, choice


def game_round():
    num1 = randint(1, 20)
    step = randint(2, 10)
    nums = [str(num1)]
    res = num1

    for num in range(9):
        res += step
        nums.append(str(res))

    correct_answer = str(choice(nums))
    num_string = ' '.join(nums).replace(correct_answer, '...')

    print(f'Question: {num_string}')
    print('Your answer: ')
    answer = input()
    if answer == correct_answer:
        return True
    else:
        print(f'"{answer}" is wrong answer ;(. '
              f'Correct answer was "{correct_answer}".')
        return False


METAINFO = {
    'round': game_round,
    'rules': 'What number is missing in the progression?'
}
