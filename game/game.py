from bodyofgame import BodyOfGame


def main():
    pontos: int = 0
    jogar(pontos)

nomes = []


def jogar(pontos):
    global nome  # noqa
    try:
        if len(nomes) == 0:
            nome = input('SEU NOME: ')
            nomes.append(nome)
            if nome == '' or nome.isnumeric():
                print('erro...')
                jogar(pontos)

        dificuldade = input(f'{nome}, ESCOLHA A DIFICULDADE: [1 - FÁCIL, 2 - MÉDIA, 3 - DIFÍCIL, 4 - MUITO DIFÍCIL] ')
        if dificuldade == '' or not dificuldade.isnumeric():
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

        ope = input(f'{nome}, ESCOLHA A OPERAÇÃO: [1 - SOMA, 2 - SUBTRAÇÃO, 3 - MULTIPLICAÇÃO] ')
        if ope == '' or not ope.isnumeric():
            print('Digite apenas números.')
            main()
        else:
            ope = int(ope)
            if ope > 3:
                print()
                print('Apenas números entre 1 e 3.')
                print()
                jogar(pontos)
                
        corpodojogo: BodyOfGame = BodyOfGame(dificuldade, ope)
        corpodojogo.gerar_operacao(ope)

    except (ValueError, TypeError, UnboundLocalError) as err:
        return f'Erros do tipo {err} encontrados.'

    print('PERGUNTA: ')
    corpodojogo.mostrar_pergunta()

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
            print(f'{nome}, Você possui {pontos} ponto.')
            print()
        else:
            print()
            print(f'{nome}, Você possui {pontos} pontos.')
            print()
        print()

    try:
        continuar = input(f'{nome}, DESEJA CONTINUAR: [1 - SIM, 2 - NÃO] ')
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
            print(f'{nome}, Você terminou o jogo com {pontos} ponto.')
            print()
        else:
            print()
            print(f'{nome}, Você terminou o jogo com {pontos} pontos.')
            print()
        exit(1)


if __name__ == '__main__':
    main()
