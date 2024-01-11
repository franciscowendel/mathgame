from bodyofgame import BodyOfGame
from time import sleep


def math_game():
    points: int = 0
    play(points)


names = []


def play(points):
    global name  # noqa
    try:
        if len(names) == 0:
            name = input('Your name: ')
            names.append(name)
            if name == '' or name.isnumeric():
                print()
                print('error...')
                print()
                sleep(0.5)
                play(points)

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
        game._create_operation(ope)

    except (ValueError, TypeError) as err:
        return f'Errors {err} found.'

    print()
    print('Question: ')
    print()
    game._show_question()

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

    if game._check_result(answer):
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
        keep_in_the_game = input(f'{name}, Want to keep in the game: [1 - Yes, 2 - No] ')
        if not keep_in_the_game.isnumeric():
            print()
            print('Type numbers.')
            print()
            sleep(0.5)
            play(points)
        else:
            keep_in_the_game = int(keep_in_the_game)
            if keep_in_the_game > 2:
                print()
                print('Only numbers between 1 and 2.')
                print()
                sleep(0.5)
                play(points)

    except (ValueError, TypeError) as err:
        return f'Errors {err} found.'

    if continuar == 1:
        jogar(pontos)
    else:
        if pontos == 1:
            print()
            print(f'{nome}, Você terminou o jogo com {pontos} ponto.')
            print()
        else:
            print()
            print(f'{nome}, Você terminou o jogo com {pontos} pontos.')
            print()
        exit(1)


if __name__ == '__main__':
    main()
