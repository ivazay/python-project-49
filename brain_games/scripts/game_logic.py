from typing import Callable


def run_game(rules: str, player_name: str, game_round: Callable[[], bool]):
    print(rules)

    for _ in range(3):
        if game_round():
            print('Correct!')
        else:
            print(f"Let's try again, {player_name}!")
            break
    else:
        print(f'Congrats, {player_name}!')
