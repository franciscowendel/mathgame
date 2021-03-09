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

    @property
    def operacao(self):
        return self._operacao

    @operacao.setter
    def operacao(self, ope):
        self._operacao = ope

    def __str__(self):
        inf = ''
        if self.operacao == 1:
            inf = '+'
        elif self.operacao == 2:
            inf = '-'
        elif self.operacao == 3:
            inf = '*'
        else:
            'Operação inválida...'
        return f'Valor1: {self.valor1}\nValor2: {self.valor2}\nDificuldade: {self.dificuldade}\nOperação: {inf}'

    def _simbolo_op(self):
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        elif self.operacao == 3:
            '*'
        else:
            return 'Erro...'

    def _gerar_valor(self):
        if self.dificuldade == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)

    def _gerar_resultado(self):
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor1
        elif self.operacao == 3:
            return self.valor1 * self.valor2
        else:
            return 'Erro...'

    def gerar_operacao(self, ope):
        if ope == 1:
            self.operacao = 1
        elif ope == 2:
            self.operacao = 2
        elif ope == 3:
            self.operacao = 3
        else:
            return 'Erro...'
        return ope
