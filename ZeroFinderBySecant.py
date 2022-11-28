import Utils as appUtils

from ZeroFinderByInterval import ZeroFinderByInterval


class ZeroFinderBySecant(ZeroFinderByInterval):

    def __init__(self, fn_):
        self.fn = fn_
        super().__init__(fn_)

    def before_init_iteration(self):
        super().before_init_iteration()
        self.result = appUtils.approach_to_zero_by_secant(self.fn, self._a_1, self._a_2)

    def solver_function(self):
        self._a_1 = self._a_2
        self._a_2 = self.result
        self.result = appUtils.approach_to_zero_by_secant(self.fn, self._a_1, self._a_2)
