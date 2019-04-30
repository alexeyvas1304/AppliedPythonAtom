#!/usr/bin/env python
# coding: utf-8


class DecisionStumpRegressor:
    '''
    Класс, реализующий решающий пень (дерево глубиной 1)
    для регрессии. Ошибку считаем в смысле MSE
    '''

    def __init__(self):
        '''
        Мы должны создать поля, чтобы сохранять наш порог th и ответы для
        x <= th и x > th
        '''
        self.th = None
        self.left = None
        self.right = None

    def fit(self, X, y):
        '''
        метод, на котором мы должны подбирать коэффициенты th, y1, y2
        :param X: массив размера (1, num_objects)
        :param y: целевая переменная (1, num_objects)
        :return: None
        '''
        X, y = zip(*sorted(zip(X, y)))
        mse_full = np.sum((y - np.mean(y)) ** 2) / len(y)
        prirost_lst = []
        for i in range(len(X) - 1):
            y_left = y[:i + 1]
            y_right = y[i + 1:]
            prirost = mse_full - (
                        np.sum((y_left - np.mean(y_left)) ** 2) + np.sum((y_right - np.mean(y_right)) ** 2)) / len(y)
            prirost_lst.append(prirost)
        idx = np.argmax(np.array(prirost_lst))
        self.th = (X[idx] + X[idx + 1]) / 2
        self.left = np.mean(y[:idx + 1])
        self.right = np.mean(y[idx + 1:])

    def predict(self, X):
        '''
        метод, который позволяет делать предсказания для новых объектов
        :param X: массив размера (1, num_objects)
        :return: массив, размера (1, num_objects)
        '''
        result = []
        for t in X:
            if t > self.th:
                result.append(self.right)
            else:
                result.append(self.left)
        return np.array(result)
