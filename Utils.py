from sympy import *
import math

x = Symbol('x')


def fprime(fn_):
    return diff(fn_(x))


def newton_raphson(value_, fn_, fprime_=None):
    if fprime_ is None: fprime_ = fprime(fn_)
    try:
        return float(value_ - (fn_(value_) / fprime_.subs([(x, value_)])))
    except (RuntimeError, TypeError, NameError, Exception):
        return None


def is_valid_number_to_operate(num_):
    if num_ is not None:
        if math.isinf(num_):
            return False
        elif math.isnan(num_):
            return False
    else:
        return False
    return True
