# -*- coding: utf-8 -*-

import json
import csv


def is_json(filename, encode):
    try:
        with open(filename, encoding=encode) as f:
            lst = json.load(f)
    except Exception:
        return None
    return True


def is_csv(filename, encode):
    with open(filename, encoding=encode) as f:
        data = csv.reader(f, delimiter="\t")
        length = 0
        for row in data:
            if length != 0 and length != len(row):
                return None
            length = len(row)
    return True


def define_format(filename, encode):
    if is_json(filename, encode):
        with open(filename, encoding=encode) as f:
            lst = json.load(f)
        if type(lst) not in [list] or len(lst) == 0 or lst == '[]\n':
            # print('Формат не валиден')
            return None

        my_set = set()
        for dic in lst:
            my_set.add(tuple(list(dic.keys())))

        if (len(my_set)) > 1:
            return None

        return 'json'
    elif is_csv(filename, encode):
        return 'csv'
    else:
        return None

# __all__ = ["define_format"]
