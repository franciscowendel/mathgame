from bodyofgame import BodyOfGame


def main():
    pontos: int = 0
    jogar(pontos)


def jogar(pontos):
    try:
        pass
    except (ValueError, TypeError, UnboundLocalError) as err:
        return f'Erro do tipo {err} encontrado'


if __name__ == '__main__':
    main()
