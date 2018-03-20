from types import FunctionType

from math import *


def xrange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step


def numeric_solve(target: float, fn: FunctionType, start, stop, inc=0.0005):
    prev = fn(start)
    for i in xrange(start - inc, stop + inc, inc):
        current = fn(i)
        if prev <= target <= current or current <= target <= prev:
            return i
        else:
            prev = current


def t0(r, theta, omega, v, g):
    f_a = lambda t: r * (sin(theta) + sin(theta + omega * t)) + v * t - (g * t ** 2) / 2
    f_b = lambda t: r * (sin(theta) - sin(theta + omega * t)) + v * t - (g * t ** 2) / 2
    x2 = (v + sqrt(v ** 2 + 2 * g * r * sin(theta))) / g
    a = numeric_solve(0, f_a, 0.1, x2)
    b = numeric_solve(0, f_b, 0.1, x2)
    print("t", a, b)
    if a and not b:
        return a
    elif b and not a:
        return b
    else:
        return min(a, b)


def v_next(coeff: float, v: float, omega: float, r: float, theta: float) -> float:
    """
    Returns the next velocity of the coin after an impact given its state and parameters

    :param coeff: Coefficient of restitution
    :param v: Velocity of coin at impact (negative)
    :param omega: Angular velocity
    :param r: Radius of coin
    :param theta: Angle of impact
    :return: Next velocity of coin
    """
    return (coeff + 1) * (v + omega * r * cos(theta)) * (sin(theta) ** 2) - v


def omega_next(coeff: float, v: float, omega: float, r: float, theta: float) -> float:
    """
    Returns the next angular velocity of the coin given state and certain parameters

    :param coeff: Coefficient of restitution
    :param v: Velocity at impact (negative)
    :param omega: Angular velocity at impact
    :param r: Radius of coin
    :param theta: Angle of impact
    :return: The next angular velocity of the coin
    """
    return -4 * (coeff + 1) / r * (v + omega * r * cos(theta)) * cos(theta) - omega


def in_equil(g: float, coeff: float, theta: float, thickness: float, radius: float, omega: float, v: float) -> bool:
    """
    Given the coin's state, returns if the coin is available to be in equilibrium on the next hit of the surface.

    :param g: Acceleration due to gravity (positive)
    :param coeff: Coefficient of restitution
    :param theta: Angle of impact
    :param thickness: Thickness of coin
    :param radius: Radius of coin
    :param omega: Angular velocity at impact
    :param v: Velocity at impact (negative)
    :return: If the coin will be in equilibrium on the next turn.
    """
    epsilon = atan2(thickness, 2 * radius)
    return g / (2 * coeff) * (theta - pi / 2 - epsilon) <= omega * v <= g / (2 * coeff) * (theta - pi / 2 + epsilon)
