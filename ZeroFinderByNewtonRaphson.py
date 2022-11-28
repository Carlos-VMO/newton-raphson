from ZeroFinder import ZeroFinder
import Utils as appUtils


class ZeroFinderByNewtonRaphson(ZeroFinder):

    __fprime = None

    def __init__(self, fn_):
        self.fn = fn_
        super().__init__(fn_)

    def before_init_iteration(self):
        super().before_init_iteration()
        self.__fprime = appUtils.fprime(self.fn)
        self.solver_function()

    def solver_function(self):
        self.result = appUtils.newton_raphson(self.result, self.fn, self.__fprime)