import Utils as appUtils

from ZeroFinderByInterval import ZeroFinderByInterval


class ZeroFinderByBisection(ZeroFinderByInterval):
    max_i = 50

    def __init__(self, fn_):
        self.fn = fn_
        super().__init__(fn_)

    def before_init_iteration(self):
        super().before_init_iteration()
        self.result = appUtils.half([self._a_1, self._a_2])

    def solver_function(self):
        if self.fn(self.result) * self.fn(self._a_1) > 0:
            self._a_1 = self.result
        else:
            self._a_2 = self.result
        self.result = appUtils.half([self._a_1, self._a_2])

    def get_zero(self):
        if self.fn(self.initial_value) * self.fn(self.initial_value_2) < 0:
            return super().get_zero()
        else:
            print('No ha sido posible encontrar un cero. Por favor verifique la función y el intervalo de busqueda')
            return
