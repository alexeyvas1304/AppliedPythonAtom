#!/usr/bin/env python
# coding: utf-8


import numpy as np


def check(arr1, arr2):
    if arr1.shape[0] != arr2.shape[0]:
        raise ValueError
    return True


def logloss(y_true, y_pred, eps=1e-8):
    """
    logloss
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    if check(y_true, y_pred):
        y_pred = np.clip(y_pred, eps, 1 - eps)
        return -sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred)) / len(y_true)


def variables(y_true, y_pred):
    # сделал втупую, мб можно красивее
    tp, tn, fp, fn = 0, 0, 0, 0
    for i in range(y_true.shape[0]):
        if y_true[i] == 1 and y_pred[i] == 1:
            tp += 1
        if y_true[i] == 0 and y_pred[i] == 0:
            tn += 1
        if y_true[i] == 0 and y_pred[i] == 1:
            fp += 1
        if y_true[i] == 1 and y_pred[i] == 0:
            fn += 1
    return tp, tn, fp, fn


def accuracy(y_true, y_pred):
    """
    Accuracy
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    if check(y_true, y_pred):
        tp, tn, fp, fn = variables(y_true, y_pred)
        return (tp + tn) / (tp + tn + fp + fn)


def presicion(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    if check(y_true, y_pred):
        tp, tn, fp, fn = variables(y_true, y_pred)
        return tp / (tp + fp)


def recall(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    if check(y_true, y_pred):
        tp, tn, fp, fn = variables(y_true, y_pred)
        return tp / (tp + fn)


def roc_auc(y_true, y_pred, step=0.001):
    """
    roc_auc
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    if check(y_true, y_pred):
        tpr = []
        fpr = []
        for threshold in np.arange(0, 1 + step, step):
            y_tmp = np.copy(y_pred)
            y_tmp[y_tmp >= threshold] = 1
            y_tmp[y_tmp < threshold] = 0
            tp, tn, fp, fn = variables(y_true, y_tmp)
            tpr.append(tp / (tp + fn))
            fpr.append(fp / (fp + tn))
            # plt.scatter (fp/(fp+tn),tp/(tp+fn))
    return -np.trapz(np.array(tpr), np.array(fpr))
