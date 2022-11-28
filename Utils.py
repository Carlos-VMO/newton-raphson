from sympy import *
import math

x = Symbol('x')


def fprime(fn_):
    return diff(fn_(x))


def newton_raphson(value_, fn_, fprime_=None):
    if fprime_ is None:
        fprime_ = fprime(fn_)
    try:
        return float(value_ - (fn_(value_) / fprime_.subs([(x, value_)])))
    except (RuntimeError, TypeError, NameError, Exception):
        return None


def approach_to_zero_by_secant(fn_, x_prev_, x_):
    return x_ - (N(fn_(x_) * (x_ - x_prev_)) / N((fn_(x_) - fn_(x_prev_))))


def is_valid_number_to_operate(num_):
    if num_ is None or (num_ is not None and (math.isinf(num_) or math.isnan(num_))):
        return False
    return True


def half(terms):
    return sum(terms) / len(terms)
