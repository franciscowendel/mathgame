from bodyofgame import BodyOfGame


def main():
    pontos: int = 0
    jogar(pontos)


def jogar(pontos):
    try:
        dificuldade = input('DIFICULDADE: [1 - FÁCIL, 2 - MÉDIA, 3 - DIFÍCIL, 4 - MUITO DIFÍCIL] ')
        if not dificuldade.isnumeric():
            print()
            print('Digite apenas números.')
            print()
            jogar(pontos)
        else:
            dificuldade = int(dificuldade)
            if dificuldade > 4:
                print()
                print('Apenas números entre 1 e 4.')
                print()
                jogar(pontos)

        ope = input('OPERAÇÃO: [1 - SOMA, 2 - SUBTRAÇÃO, 3 - MULTIPLICAÇÃO, 4 - DIVISÃO] ')
        if not ope.isnumeric():
            print('Digite apenas números.')
            main()
        else:
            ope = int(ope)
            if ope > 4:
                print()
                print('Apenas números entre 1 e 3.')
                print()
                jogar(pontos)

    except (ValueError, TypeError, UnboundLocalError) as err:
        return f'Erros do tipo {err} encontrados.'

    corpodojogo: BodyOfGame = BodyOfGame(dificuldade, ope)

    corpodojogo.gerar_operacao(ope)

    print('DIGITE A RESPOSTA: ')
    corpodojogo.mostrar_operacao()

    try:
        resposta = input()
        if not resposta.isnumeric():
            print('Digite apenas números.')
            jogar(pontos)
        else:
            resposta = int(resposta)

    except (ValueError, TypeError, UnboundLocalError) as err:
        return f'Erros do tipo {err} encontrados.'

    if corpodojogo.checar_resultado(resposta):
        pontos += dificuldade
        print()
        if pontos == 1:
            print()
            print(f'Você possui {pontos} ponto.')
            print()
        else:
            print()
            print(f'Você possui {pontos} pontos.')
            print()
        print()

    try:
        continuar = input('DESEJA CONTINUAR: [1 - SIM, 2 - NÃO] ')
        if not continuar.isnumeric():
            print()
            print('Digite apenas números.')
            print()
            jogar(pontos)
        else:
            continuar = int(continuar)
            if continuar > 2:
                print()
                print('Apenas números entre 1 e 2.')
                print()
                jogar(pontos)

    except (ValueError, TypeError, UnboundLocalError) as err:
        return f'Erros do tipo {err} encontrados.'

    if continuar == 1:
        jogar(pontos)
    else:
        if pontos == 1:
            print()
            print(f'Você terminou o jogo com {pontos} ponto.')
            print()
        else:
            print()
            print(f'Você terminou o jogo com {pontos} pontos.')
            print()
        exit(1)


if __name__ == '__main__':
    main()
