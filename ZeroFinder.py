import Utils as appUtils

from abc import ABC, abstractmethod

class ZeroFinder(ABC):
    __tolerance = 1E-15
    __max_i = 10
    __initial_value = 1
    __fn = None
    __result = 0

    def __init__(self, fn_):
        self.fn = fn_

    @property
    def initial_value(self):
        return self.__initial_value

    @initial_value.setter
    def initial_value(self, initial_value_):
        self.__initial_value = initial_value_

    @property
    def tolerance(self):
        return self.__tolerance

    @tolerance.setter
    def tolerance(self, tolerance_):
        self.__tolerance = tolerance_

    @property
    def max_i(self):
        return self.__max_i

    @max_i.setter
    def max_i(self, max_i_):
        self.__max_i = max_i_

    @property
    def fn(self):
        return self.__fn

    @fn.setter
    def fn(self, fn_):
        if fn_ is None:
            print('No se puede asignar una función nula.')
            return
        self.__fn = fn_

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, result_):
        self.__result = result_

    def before_init_iteration(self):
        self.result = self.initial_value

    def init_iteration(self, callback_):
        self.before_init_iteration()
        i = 0
        while appUtils.is_valid_number_to_operate(self.result) and \
                abs(self.fn(self.result)) > self.tolerance and i <= self.max_i:
            i += 1
            callback_()

    def get_zero(self):
        self.init_iteration(self.solver_function)
        return self.result

    @abstractmethod
    def solver_function(self):
        pass
