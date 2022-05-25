import matplotlib.pyplot as plt
import numpy as np  # для работы с массивами


def graph_builder(func, a, b, root, eps, title="Root finding", save=False):
    """Строит график функции 
        и отмечает корень"""

    # иксы и игреки на интервале [a,b]
    x = np.arange(a, b, 0.01)
    y = [func(i) for i in x]

    # значение функции в корне
    fc = func(root)
    min_y, max_y = min(y), max(y)
    min_x, max_x = min(x), max(x)

    # заголовок графика
    plt.title(title)

    plt.plot(x, y, label="Function")  # граифк функции
    # plt.gca().set_aspect('equal', adjustable='box')

    plt.plot([min_x, max_x], [0, 0], color="blue", label="X, Y")
    plt.plot([0, 0], [min_y, max_y], color="blue")

    # ориентиры для корня на графике
    plt.plot([a, b], [fc, fc], color="orange", linestyle="dashed")
    plt.plot([root, root], [min_y, max_y], color="orange",
             linestyle="dashed")

    # отмечаем точку корня на графике
    plt.scatter(([root]), ([fc]), s=70, zorder=3, color="red",
                label="root: x = {:.4f}\n"
                      "{tab}y = {:.4f}\nEPS={}".format(root, func(root), eps, tab=8 * " "))

    plt.legend()  # отображаем подписи

    plt.show()  # показываем график
