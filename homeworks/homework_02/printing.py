# -*- coding: utf-8 -*-

import json
import csv


def to_list(file, encode, formats):
    if formats == 'json':
        with open(file, encoding=encode) as f:
            lst_json = json.load(f)
        lst = [[] for i in range(len(lst_json) + 1)]
        for k in lst_json[0].keys():
            lst[0].append(str(k))
        for i in range(0, len(lst_json)):
            for v in lst_json[i].values():
                lst[i + 1].append(str(v))
    elif formats == 'csv':
        with open(file, encoding=encode) as f:
            data = csv.reader(f, delimiter="\t")
            lst = []
            for item in data:
                lst.append(item)
    return lst


def print_table(file, encode, formats):
    lst = to_list(file, encode, formats)
    if lst == []:
        print('Формат не валиден')
        return None
    rows = len(lst)
    columns = len(lst[0])

    if columns == 0:
        print('Формат не валиден')
        return None


    lst_maxlen = []
    if rows == 1:
        for word in lst[0]:
            lst_maxlen.append(len(str(word)))
    if rows > 1:
        for i in range(columns):
            maxlen = 0
            for j in range(rows):
                if len(str(lst[j][i])) > maxlen:
                    maxlen = len(str(lst[j][i]))
            lst_maxlen.append(maxlen)
    for i in range(columns):
        lst_maxlen[i] += 4
    print((sum(lst_maxlen) + columns + 1) * '-')
    for i in range(columns):
        print('|' + '{:^{}}'.format(lst[0][i], lst_maxlen[i]), end='')
    print('|')
    for i in range(1, rows):
        for j in range(columns - 1):
            print('|  ' + str(lst[i][j]) +
                  (lst_maxlen[j] - 2 - len(str(lst[i][j]))) * ' ', end='')
        print('|', end='')

        print('{:>{}}'.format(lst[i][columns - 1] + '  ',
                              lst_maxlen[columns - 1]), end='')
        print('|')
    print((sum(lst_maxlen) + columns + 1) * '-')

# __all__ = ["print_table"]
