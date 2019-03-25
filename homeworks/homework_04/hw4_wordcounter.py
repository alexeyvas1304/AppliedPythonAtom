#!/usr/bin/env python
# coding: utf-8

import os
from multiprocessing import Pool, Manager

result_dict = Manager().dict()


def counter(full_path):
    cnt = 0
    with open(full_path, 'r') as f:
        for line in f.readlines():
            cnt += len(line.split())
    result_dict[full_path.split('/')[-1]] = cnt


def word_count_inference(path_to_dir):
    '''
    Метод, считающий количество слов в каждом файле из директории
    и суммарное количество слов.
    Слово - все, что угодно через пробел, пустая строка "" словом не считается,
    пробельный символ " " словом не считается. Все остальное считается.
    Решение должно быть многопроцессным. Общение через очереди.
    :param path_to_dir: путь до директории с файлами
    :return: словарь, где ключ - имя файла, значение - число слов +
        специальный ключ "total" для суммы слов во всех файлах
    '''

    lst = map(lambda path_file: path_to_dir + '/' + path_file, os.listdir(path=path_to_dir))
    with Pool(3) as p:
        p.map(counter, lst)
    result_dict['total'] = sum(result_dict.values())
    return result_dict
