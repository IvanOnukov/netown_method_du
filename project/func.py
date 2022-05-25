import sympy

from sympy.parsing.sympy_parser import parse_expr

# log(x+2.0) - x**4.0 + 0.5
# x**2 - e**-(x)


def func(x_in, form='log(x+2.0) - x**4.0 + 0.5'):
    expr = parse_expr(form)
    x = sympy.symbols('x')
    f = sympy.lambdify(x, expr, 'numpy')
    return float(f(x_in))


def func_dif(x_in, form='log(x+2.0) - x**4.0 + 0.5'):
    expr = parse_expr(form)
    x = sympy.symbols('x')
    dx = expr.diff(x)
    f = sympy.lambdify(x, dx, 'numpy')
    return float(f(x_in))

