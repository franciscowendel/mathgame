from random import randint


class BodyOfGame:

    def __init__(self, dificuldade: int, ope) -> None:
        self.__dificuldade: int = dificuldade
        self.__ope = self.gerar_operacao(ope)
        self.__valor1: int = self._gerar_valor()
        self.__valor2: int = self._gerar_valor()
        self.__resultado: int = self._gerar_resultado()
        self._operacao = self.gerar_operacao(ope)

    @property
    def dificuldade(self) -> int:
        return self.__dificuldade

    @property
    def ope(self):
        return self.__ope

    @property
    def valor1(self) -> int:
        return self.__valor1

    @property
    def valor2(self) -> int:
        return self.__valor2

    @property
    def resultado(self) -> int:
        return self.__resultado

