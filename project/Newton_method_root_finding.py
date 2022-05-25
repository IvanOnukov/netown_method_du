import os
import sys

from func import *  # аналитическая функция
from plot_func import *  # для построения графика

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def within_eps(a, b, eps):
    """Проверка равности чисел a и b с заданной точностью eps"""
    # return ((a - eps) < b) and (b < (a + eps))
    return abs(a - b) < eps


def newton_root_finding_method(function, function_dif, a, b, eps=0.01, form='log(x+2.0) - x**4.0 + 0.5', max_iter=200):
    x_next = (a + b) / 2  # начальное приближение
    x_prev = x_next  # запоминаем предыдущее значение

    iter_count = 0
    while True:
        try:
            x_next = x_next - function(x_next, form) / function_dif(x_next, form)
        except ZeroDivisionError:
            print("Error! - производная равна 0  x = ", x_next)
            sys.exit(1)

        print("{:.5f} - {:.5f} / {:.5f}".format(x_prev, function(x_next, form), function_dif(x_next, form)))
        print("x_next: {:.5f}".format(x_next))  # печатаем его

        iter_count + 1
        '''если модуль разницы текущего
            и предудыщего значения
            меньше чем эпсилон
            или превышено кол-во итераций
        '''
        if within_eps(x_next, x_prev, eps) or iter_count > max_iter:
            print("diff = x_next - x_prev = {:.5f} - {:.5f} = {:.7f}".format(x_next, x_prev, abs(x_prev - x_next)))
            # выходим
            break

        x_prev = x_next  # запоминаем предыдущее значение

    return x_next


if __name__ == "__main__":

    path = "test_data/test1"

    file = open(path, 'r')
    try:
        form = file.read()
    finally:
        file.close()

    a1 = 0.5
    b1 = a1 + 0.5
    eps1 = 0.001

    root = newton_root_finding_method(func, func_dif, a1, b1, eps1, form)

    print("root: {:.7f}".format(root))
    graph_builder(func, -0.5, 2, root, eps1, title="Finding root using Newthon method", save=True)