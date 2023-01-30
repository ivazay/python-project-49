from prompt import string


def welcome_user():
    name = string("What's your name?")
    print(f'Hello, {name}!')
