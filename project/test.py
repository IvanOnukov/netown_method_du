import math

import sympy

from sympy.parsing.sympy_parser import parse_expr


def func_(x_in, form='log(x+2.0) - x**4.0 + 0.5'):
    expr = parse_expr(form)
    x = sympy.symbols('x')
    f = sympy.lambdify(x, expr, 'numpy')
    return f(x_in)


def func_dif(x_in, form='log(x + 2.0) - x ** 4.0 + 0.5'):
    expr = parse_expr(form)
    x = sympy.symbols('x')
    y = expr.diff(x)
    f = sympy.lambdify(x, y, 'numpy')
    print(f(x_in))


def func(x):
    """Аналитически заданная функция"""
    return math.log(x + 2.0) - x ** 4.0 + 0.5


def func_deriv(x):
    """ПРоизводная аналитически заданной функции"""
    return 1.0 / (x + 2) - 4.0 * x ** 3.0


import numpy as np
from scipy.interpolate import RectBivariateSpline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return exp(-(2.0*x)**2.0 - (y/2.0)**2.0)


if __name__ == "__main__":
    # Regularly-spaced, coarse grid
    dx, dy = 0.4, 0.4
    xmax, ymax = 2, 4
    x = np.arange(-xmax, xmax, dx)
    y = np.arange(-ymax, ymax, dy)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-(2 * X) ** 2 - (Y / 2) ** 2)

    interp_spline = RectBivariateSpline(y, x, Z)

    # Regularly-spaced, fine grid
    dx2, dy2 = 0.16, 0.16
    x2 = np.arange(-xmax, xmax, dx2)
    y2 = np.arange(-ymax, ymax, dy2)
    X2, Y2 = np.meshgrid(x2, y2)
    Z2 = interp_spline(y2, x2)

    fig, ax = plt.subplots(nrows=1, ncols=2, subplot_kw={'projection': '3d'})
    ax[0].plot_wireframe(X, Y, Z, color='k')

    ax[1].plot_wireframe(X2, Y2, Z2, color='k')
    for axes in ax:
        axes.set_zlim(-0.2, 1)
        axes.set_axis_off()

    fig.tight_layout()
    plt.show()