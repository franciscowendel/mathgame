from bodyofgame import BodyOfGame


def main():
    pontos: int = 0
    jogar(pontos)


def jogar(pontos):
    try:
        dificuldade: int = int(input('DIFICULDADE: [1 - FÁCIL, 2 - MÉDIA, 3 - DIFÍCIL, 4 - MUITO DIFÍCIL] '))
        ope: int = int(input('OPERAÇÃO: [1 - SOMA, 2 - SUBTRAÇÃO, 3 - MULTIPLICAÇÃO]'))
        if ope > 3:
            print('Operação inválida...')
            main()

    except (ValueError, TypeError, UnboundLocalError) as err:
        return f'Erro do tipo {err} encontrado'

    corpodojogo: BodyOfGame = BodyOfGame(dificuldade, ope)

    corpodojogo.gerar_operacao(ope)

    print()
    print('DIGITE A RESPOSTA: ')
    corpodojogo.mostrar_operacao()

    try:
        resposta: int = int(input())

    except (ValueError, TypeError, UnboundLocalError) as err:
        return f'Erro do tipo {err} encontrado'

    if corpodojogo.checar_resultado(resposta):
        pontos += dificuldade
        print()
        print(f'Você possui {pontos} ponto(s)')


if __name__ == '__main__':
    main()
