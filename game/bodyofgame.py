from random import randint


class BodyOfGame:

    def __init__(self, difficulty: int, ope) -> None:
        self.__difficulty: int = difficulty
        self.__ope = self._create_operation(ope)
        self.__value_1: int = self._create_value()
        self.__value_2: int = self._create_value()
        self.__result: int = self._create_result()
        self._operation = None

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
        """Creates the values of the game according to difficulty chosen by the user."""
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

    def _create_result(self) -> int:
        """Creates the final result according to the created values and the chosen operation."""
        if self.operation == 1:
            return self.value_1 + self.value_2
        elif self.operation == 2:
            if self.value_1 < self.value_2:
                return self.value_2 - self.value_1
            else:
                return self.value_1 - self.value_2
        elif self.operation == 3:
            return self.value_1 * self.value_2
        else:
            raise ValueError('error...')

    def _create_operation(self, ope):
        """Assures that the right operation is set."""
        if ope == 1:
            self.operation = 1
        elif ope == 2:
            self.operation = 2
        elif ope == 3:
            self.operation = 3
        else:
            raise ValueError('error...')
        return ope

    def _check_result(self, answer) -> bool:
        """Checks if the result is the same as the answer given by the user."""
        verify: bool = False

        if self.result == answer:
            print()
            print('Congratulations, you are right! :)')
            print()
            verify: bool = True
        else:
            print()
            print('Unfortunately, you are wrong! :(')
            print()
        if self.value_1 < self.value_2:
            print()
            print(f'{self.value_2} {self._symbol_operation()} {self.value_1} = {self.result}')
            print()
        else:
            print()
            print(f'{self.value_1} {self._symbol_operation()} {self.value_2} = {self.result}')
            print()
        return verify

    def _show_question(self):
        """Shows the question to the user."""
        if self.value_1 < self.value_2:
            print()
            print(f'{self.value_2} {self._symbol_operation()} {self.value_1} = ?')
            print()
        else:
            print()
            print(f'{self.value_1} {self._symbol_operation()} {self.value_2} = ?')
            print()
