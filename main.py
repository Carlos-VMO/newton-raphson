from sympy import *

from ZeroFinderByBisection import ZeroFinderByBisection
from ZeroFinderByFalsePosition import ZeroFinderByFalsePosition
from ZeroFinderByNewtonRaphson import ZeroFinderByNewtonRaphson
from ZeroFinderBySecant import ZeroFinderBySecant

if __name__ == '__main__':
    zeroFinderByNewtonRaphson = ZeroFinderByNewtonRaphson(lambda x_: (x_ ** 2) - (4.9 * x_) + (5.7 * cos(0.01 * x_)))
    zeroFinderByNewtonRaphson.max_i = 10
    print('Por newton raphson', zeroFinderByNewtonRaphson.get_zero())

    zeroFinderByNewtonRaphson.fn = lambda x_: (x_ ** 2) - (6.8 * (x_ ** 1.01)) + 9
    print('Por newton raphson', zeroFinderByNewtonRaphson.get_zero())

    zeroFinderByBisection = ZeroFinderByBisection(lambda x_: (x_ ** 2) - (4.9 * x_) + (5.7 * cos(0.01 * x_)))
    zeroFinderByBisection.max_i = 10
    print('Por bisección', zeroFinderByBisection.get_zero())

    zeroFinderByBisection.fn = lambda x_: (x_ ** 2) - (6.8 * (x_ ** 1.01)) + 9
    print('Por bisección', zeroFinderByBisection.get_zero())

    zeroFinderBySecant = ZeroFinderBySecant(lambda x_: (x_ ** 2) - (4.9 * x_) + (5.7 * cos(0.01 * x_)))
    zeroFinderBySecant.max_i = 10
    print('Por secante', zeroFinderBySecant.get_zero())

    zeroFinderBySecant.fn = lambda x_: (x_ ** 2) - (6.8 * (x_ ** 1.01)) + 9
    print('Por secante', zeroFinderBySecant.get_zero())

    zeroFinderByFalsePosition = ZeroFinderByFalsePosition(lambda x_: (x_ ** 2) - (4.9 * x_) + (5.7 * cos(0.01 * x_)))
    zeroFinderByFalsePosition.max_i = 10
    print('Por falsa posición', zeroFinderByFalsePosition.get_zero())

    zeroFinderByFalsePosition.fn = lambda x_: (x_ ** 2) - (6.8 * (x_ ** 1.01)) + 9
    print('Por falsa posición', zeroFinderByFalsePosition.get_zero())
