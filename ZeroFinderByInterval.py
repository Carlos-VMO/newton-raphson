from ZeroFinder import ZeroFinder


class ZeroFinderByInterval(ZeroFinder):
    __initial_value_2 = 2
    _a_1 = 0
    _a_2 = 0

    @property
    def initial_value_2(self):
        return self.__initial_value_2

    @initial_value_2.setter
    def initial_value_2(self, initial_value_2):
        self.__initial_value_2 = initial_value_2

    def __init__(self, fn_):
        self.fn = fn_
        super().__init__(fn_)

    def before_init_iteration(self):
        self._a_1 = self.initial_value
        self._a_2 = self.initial_value_2

    def solver_function(self):
        pass
