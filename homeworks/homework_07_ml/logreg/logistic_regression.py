#!/usr/bin/env python
# coding: utf-8


import numpy as np


class LogisticRegression:
    def __init__(self, lambda_coef=0.1, regularization=None, alpha=0.3, eps=0.0001, iterations=5000, flag=False):
        """
        LogReg for Binary case
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
        if X.shape[0] != y.shape[0]:
            raise ValueError
        return True

    def fit(self, X_train, y_train):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        if self.check(X_train, y_train):
            n = X_train.shape[0]
            k = X_train.shape[1]
            self.mean_x = np.mean(X_train, axis=0)
            self.std_x = np.std(X_train, axis=0)
            X_train = (X_train - self.mean_x) / self.std_x
            X_train = np.hstack([np.ones((n, 1)), X_train])
            self.w = np.random.randn(k + 1, 1)
            cnt = 0
            while True:
                sigm_dist = 1 / (1 + np.exp(-X_train @ self.w))
                deriv_const = 1 / n * (X_train.T @ (sigm_dist - y_train.reshape(n, 1))).T
                if self.regularization == 'L1':
                    add = self.alpha * np.sign(self.w).reshape(1, -1)
                elif self.regularization == 'L2':
                    add = 2 * self.alpha * self.w.T
                else:
                    add = 0
                full_deriv = deriv_const + add
                tmp = self.w
                self.w = self.w - self.lambda_coef * full_deriv.T
                cnt += 1
                if np.sum((tmp - self.w) ** 2) < self.eps or cnt == self.iterations:
                    break
            self.flag = True
            return None

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        if not self.flag:
            raise Exception()
        probabilities = self.predict_proba(X_test).reshape(-1)
        y_test = np.zeros(probabilities.shape[0])
        y_test[probabilities >= 0.5] = 1
        return y_test

    def predict_proba(self, X_test):
        """
        Predict probability using model.
        :param X_test: test data for predict in
        :return: y_test: predicted probabilities
        """
        if not self.flag:
            raise Exception()
        n = X_test.shape[0]
        k = X_test.shape[1]
        X_test = (X_test - self.mean_x) / self.std_x
        X_test = np.hstack([np.ones((n, 1)), X_test])
        weights = self.get_weights()
        return 1 / (1 + np.exp(-(X_test @ weights)))

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        if not self.flag:
            raise Exception()
        return self.w
