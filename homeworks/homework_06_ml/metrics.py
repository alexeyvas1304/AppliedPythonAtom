#!/usr/bin/env python
# coding: utf-8


import numpy as np


def check(y_true, y_hat):
    if type(y_true) != np.ndarray or type(y_hat) != np.ndarray:
        print('invalid data')
        return False
    if y_true.shape[0] != y_hat.shape[0]:
        print('bad size')
        return False
    return True


def mse(y_true, y_hat, derivative=False):
    """
    Mean squared error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    if check(y_true, y_hat):
        return sum((y_true - y_hat) ** 2) / y_true.shape[0]


def mae(y_true, y_hat):
    """
    Mean absolute error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    if check(y_true, y_hat):
        return sum(abs(y_true - y_hat)) / y_true.shape[0]


def r2_score(y_true, y_hat):
    """
    R^2 regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    if check(y_true, y_hat):
        ssres = sum((y_true - y_hat) ** 2)
        sstot = sum((y_true - np.mean(y_true)) ** 2)
        return 1 - SSres / SStot
