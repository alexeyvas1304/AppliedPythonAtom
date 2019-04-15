#!/usr/bin/env python
# coding: utf-8

import numpy as np


class LinearRegression:

    def __init__(self, lambda_coef=0.0005, regularization=None, alpha=0.5, eps=0.001, iterations=25000, flag=0):
        """
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.lambda_coef = lambda_coef
        self.regularization = regularization
        self.eps = eps
        self.alpha = alpha
        self.iterations = iterations
        self.flag = flag

    def check(self, X, y):
        return X.shape[0] == y.shape[0]

    def fit(self, X_train, y_train):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """

        if not self.check(X_train, y_train):
            return 'Error'

        n = X_train.shape[0]
        k = X_train.shape[1]
        self.mean_x = np.mean(X_train, axis=0)
        self.std_x = np.std(X_train, axis=0)
        X_train = (X_train - self.mean_x) / self.std_x
        X_train = np.hstack([np.ones((n, 1)), X_train])
        self.w = np.random.randn(k + 1, 1)
        cnt = 0
        while True:
            deriv_const = -2 * y_train.T @ X_train + 2 * self.w.T @ X_train.T @ X_train
            if self.regularization == 'L1':
                # надеюсь это хоть как-то работает
                add = self.alpha * np.sign(self.w).reshape(1, -1)
            elif self.regularization == 'L2':
                add = 2 * self.alpha * self.w.T
            else:
                add = np.zeros((1, k + 1))
            full_deriv = deriv_const + add  # 1*(k+1)
            tmp = self.w
            self.w = self.w - self.lambda_coef * full_deriv.T
            cnt += 1
            if np.sum(abs(tmp - self.w)) < self.eps or cnt == self.iterations:
                break
        self.flag = 1
        return None

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        if self.flag == 0:
            raise Exception()
        n = X_test.shape[0]
        k = X_test.shape[1]
        # тут надо бы проверочку на соответствие размеров трейна и теста - ну да ладно
        X_test = (X_test - self.mean_x) / self.std_x
        X_test = np.hstack([np.ones((n, 1)), X_test])
        return X_test @ self.w

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        if self.flag == 0:
            raise Exception()
        return self.w
