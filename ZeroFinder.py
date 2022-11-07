import Utils as appUtils


class ZeroFinder:
    __tolerance = 1E-15
    __max_i = 200
    __initial_value = 1
    __fn = None

    def __init__(self, fn_=None):
        if fn_ is not None: self.fn = fn_

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
        self.__fn = fn_

    def get_zero(self):
        i = 0
        initial_value = self.initial_value
        fprime = appUtils.fprime(self.fn)
        while initial_value is not None and abs(self.fn(initial_value)) > self.tolerance and i <= self.max_i:
            i += 1
            initial_value = appUtils.newton_raphson(initial_value, self.fn, fprime)
            if not appUtils.is_valid_number_to_operate(initial_value):
                break
        return initial_value
