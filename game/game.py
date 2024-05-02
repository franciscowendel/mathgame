from bodyofgame import BodyOfGame
from time import sleep


def mathgame():
    points: int = 0
    play(points)


users = []


def play(points):
    global name  # noqa
    try:
        if len(users) == 0:
            name = input('Your name: ')
            if name == '' or name.isnumeric():
                print()
                print('error...')
                print()
                sleep(0.5)
                play(points)
            else:
                users.append(name)

        difficulty = input(f'{name}, Choose the difficulty: [1 - Easy, 2 - Medium, 3 - Hard, 4 - Expert] ')
        if difficulty == '' or not difficulty.isnumeric():
            print()
            print('Type numbers.')
            print()
            sleep(0.5)
            play(points)
        else:
            difficulty = int(difficulty)
            if difficulty > 4:
                print()
                print('Only numbers between 1 and 4.')
                print()
                sleep(0.5)
                play(points)

        ope = input(f'{name}, Choose the math operation: [1 - Sum, 2 - Subtraction, 3 - Multiplication] ')
        if ope == '' or not ope.isnumeric():
            print()
            print('Type numbers.')
            print()
            sleep(0.5)
            play(points)
        else:
            ope = int(ope)
            if ope > 3:
                print()
                print('Only numbers between 1 and 3.')
                print()
                sleep(0.5)
                play(points)
                
        game: BodyOfGame = BodyOfGame(difficulty, ope)
        game._create_operation(ope) # noqa

    except (ValueError, TypeError) as err:
        return f'Errors {err} found.'

    print()
    print(f"{name}, here's the question: ")
    print()
    game._show_question() # noqa

    try:
        answer = input()
        if not answer.isnumeric():
            print()
            print('Only numbers.')
            print()
            sleep(0.5)
            play(points)
        else:
            answer = int(answer)

    except (ValueError, TypeError) as err:
        return f'Errors {err} found.'

    if game._check_result(answer): # noqa
        points += difficulty
        print()
        if points == 1:
            print()
            print(f'{name}, so far you have {points} point.')
            print()
        else:
            print()
            print(f'{name}, so far you have {points} points.')
            print()
        print()

    try:
        continue_in_the_game = input(f'{name}, Want to continue in the game: [1 - Yes, 2 - No] ')
        if not continue_in_the_game.isnumeric():
            print()
            print('Type numbers.')
            print()
            sleep(0.5)
            play(points)
        else:
            continue_in_the_game = int(continue_in_the_game)
            if continue_in_the_game > 2:
                print()
                print('Only numbers between 1 and 2.')
                print()
                sleep(0.5)
                play(points)

    except (ValueError, TypeError) as err:
        return f'Errors {err} found.'

    if continue_in_the_game == 1:
        play(points)
    else:
        if points == 0:
            print()
            print(f'{name}, you finished the game with {points} points.')
            print()
            exit(1)

        elif points == 1:
            print()
            print(f'{name}, you finished the game with {points} point.')
            print()
            exit(2)

        else:
            print()
            print(f'{name}, you finished the game with {points} points.')
            print()
            exit(3)



if __name__ == '__main__':
    mathgame()
