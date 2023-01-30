import prompt


def get_name():
    player_name = prompt.string("What's your name? ")
    return player_name


def welcome_user():
    print(f'Hello, {get_name()}!')
