from random import randint


class BodyOfGame:

    def __init__(self, difficulty: int, ope) -> None:
        self.__difficulty: int = difficulty
        self.__ope = self._create_operation(ope)
        self.__value_1: int = self._create_value()
        self.__value_2: int = self._create_value()
        self.__result: int = self._create_result()
        self._operation = self.ope

    @property
    def difficulty(self) -> int:
        return self.__difficulty

    @property
    def ope(self):
        return self.__ope

    @property
    def value_1(self) -> int:
        return self.__value_1

    @property
    def value_2(self) -> int:
        return self.__value_2

    @property
    def result(self) -> int:
        return self.__result

    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, ope):
        self._operation = ope

    def _symbol_operation(self):
        """Shows the math operation in both 'check_result' and 'show_question' methods."""
        if self.operation == 1:
            return '+'
        elif self.operation == 2:
            return '-'
        elif self.operation == 3:
            return '*'
        else:
            raise ValueError('error...')

    def _create_value(self) -> int:
        """Create the values of the game according to difficulty chosen by the user."""
        if self.difficulty == 1:
            return randint(0, 10)
        elif self.difficulty == 2:
            return randint(0, 100)
        elif self.difficulty == 3:
            return randint(0, 1000)
        elif self.difficulty == 4:
            return randint(0, 10000)
        else:
            raise ValueError('error...')

    def _gerar_resultado(self) -> int:
        """Gera o resultado final de acordo com os valores criados e a operação escolhida."""
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            if self.valor1 < self.valor2:
                return self.valor2 - self.valor1
            else:
                return self.valor1 - self.valor2
        elif self.operacao == 3:
            return self.valor1 * self.valor2
        else:
            raise ValueError('erro...')

    def gerar_operacao(self, ope):
        """Faz com que o usuário possa 'settar' uma operação específica."""
        if ope == 1:
            self.operacao = 1
        elif ope == 2:
            self.operacao = 2
        elif ope == 3:
            self.operacao = 3
        else:
            raise ValueError('erro...')
        return ope

    def checar_resultado(self, resposta) -> bool:
        """Checa se o resultado criado pelo método '_gerar_resultado' é igual ao dado pelo usuário."""
        verify: bool = False

        if self.resultado == resposta:
            print()
            print('RESPOSTA CORRETA!')
            verify: bool = True
        else:
            print('RESPOSTA INCORRETA!')
        if self.valor1 < self.valor2:
            print(f'{self.valor2} {self._simbolo_op()} {self.valor1} = {self.resultado}')
        else:
            print(f'{self.valor1} {self._simbolo_op()} {self.valor2} = {self.resultado}')
        return verify

    def mostrar_pergunta(self):
        """Mostra os valores criados e a operação escolhida pelo usuário em forma de pergunta."""
        if self.valor1 < self.valor2:
            print(f'{self.valor2} {self._simbolo_op()} {self.valor1} = ?')
        else:
            print(f'{self.valor1} {self._simbolo_op()} {self.valor2} = ?')
