#!/usr/bin/env python
# coding: utf-8

import numpy as np


def simplex_method(a, b, c):
    """
    Почитать про симплекс метод простым языком:
    * https://  https://ru.wikibooks.org/wiki/Симплекс-метод._Простое_объяснение
    Реализацию алгоритма взять тут:
    * https://youtu.be/gRgsT9BB5-8 (это ссылка на 1-ое из 5 видео).

    Используем numpy и, в целом, векторные операции.

    a * x.T <= b
    c * x.T -> max
    :param a: np.array, shape=(n, m)
    :param b: np.array, shape=(n, 1)
    :param c: np.array, shape=(1, m)
    :return x: np.array, shape=(1, m)
    """

    n, m = a.shape
    c *= -1
    matrix = np.hstack([np.vstack([a, c]),
                        np.eye(n + 1),
                        np.vstack([b.reshape(n, 1), np.array([0])])])

    def subtr(a, b, f):  # пеп ругался на лямбду, поэтому сделал отдельную функцию
        return a - b * a[f] / b[f]

    while True:
        if all(matrix[-1] >= 0):
            break
        column_index = matrix[-1].argmin()
        seq = matrix[:-1, -1] / matrix[:-1, column_index]
        row_index = seq.argmin()

        for i in range(n + 1):
            if i != row_index:
                matrix[i] = subtr(matrix[i], matrix[row_index], column_index)
            else:
                matrix[i] /= matrix[row_index][column_index]

        x = np.zeros(m)
        for i in range(m):
            if matrix[-1][i] == 0:
                index_of_1 = matrix[:, i].argmax()
                x[i] = matrix[index_of_1][-1]
    return x
