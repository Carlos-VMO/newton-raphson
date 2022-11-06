from ZeroFinder import ZeroFinder
from sympy import *

if __name__ == '__main__':
    zeroFinder = ZeroFinder()

    zeroFinder.fn = lambda x_: x_ ** 5 - 6
    print(zeroFinder.get_zero())

    zeroFinder.fn = lambda x_: x_ ** 3 - 2
    print(zeroFinder.get_zero())

    zeroFinder.fn = cos
    print(zeroFinder.get_zero())
