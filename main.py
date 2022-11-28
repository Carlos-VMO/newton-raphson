from sympy import *

from ZeroFinderByBisection import ZeroFinderByBisection
from ZeroFinderByNewtonRaphson import ZeroFinderByNewtonRaphson
from ZeroFinderBySecant import ZeroFinderBySecant

if __name__ == '__main__':
    zeroFinder = ZeroFinderByNewtonRaphson(lambda x_: x_ ** 5 - 6)
    print(zeroFinder.get_zero())

    zeroFinder.fn = lambda x_: x_ ** 3 - 2
    print(zeroFinder.get_zero())

    zeroFinder.fn = cos
    print(zeroFinder.get_zero())

    zeroFinder.fn = lambda x_: (x_ ** 2) - (4.9 * x_) + (5.7 * cos(0.01 * x_))
    print(zeroFinder.get_zero())

    zeroFinder = ZeroFinderByBisection(lambda x_: x_ ** 5 - 6)
    print(zeroFinder.get_zero())

    zeroFinder.fn = lambda x_: x_ ** 3 - 2
    print(zeroFinder.get_zero())

    zeroFinder.fn = cos
    print(zeroFinder.get_zero())

    zeroFinder.fn = lambda x_: (x_ ** 2) - (4.9 * x_) + (5.7 * cos(0.01 * x_))
    print(zeroFinder.get_zero())

    zeroFinder = ZeroFinderBySecant(lambda x_: x_ ** 5 - 6)
    print(zeroFinder.get_zero())

    zeroFinder.fn = lambda x_: x_ ** 3 - 2
    print(zeroFinder.get_zero())

    zeroFinder.fn = cos
    print(zeroFinder.get_zero())

    zeroFinder.fn = lambda x_: (x_ ** 2) - (4.9 * x_) + (5.7 * cos(0.01 * x_))
    print(zeroFinder.get_zero())
