import prompt
from argparse import ArgumentParser
from brain_games.scripts.brain_even import METAINFO as even_info
from brain_games.scripts.brain_calc import METAINFO as calc_info
from brain_games.scripts.brain_gcd import METAINFO as gcd_info
from brain_games.scripts.brain_prog import METAINFO as prog_info
from brain_games.scripts.brain_prime import METAINFO as prime_info
from brain_games.scripts.game_logic import run_game

GAMES = {
    'brain-even': even_info,
    'brain-calc': calc_info,
    'brain-gcd': gcd_info,
    'brain-prog': prog_info,
    'brain-prime': prime_info
}


def main():
    parser = ArgumentParser()
    parser.add_argument('game_name', choices=GAMES.keys())
    args = parser.parse_args()
    game_name = args.game_name
    print("Welcome to Brain Games!\n")
    player_name = prompt.string("What's your name? ")
    print(f'Hello, {player_name}!')
    # print('Chose game')
    run_game(GAMES[game_name]['rules'], player_name, GAMES[game_name]['round'])


if __name__ == '__main__':
    main()
