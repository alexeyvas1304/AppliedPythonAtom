#!/usr/bin/env python
# coding: utf-8


class HashMap:
    '''
    Давайте сделаем все объектненько,
     поэтому внутри хешмапы у нас будет Entry
    '''

    class Entry:
        def __init__(self, key, value):
            '''
            Сущность, которая хранит пары ключ-значение
            :param key: ключ
            :param value: значение
            '''
            self.key = key
            self.value = value

        def get_key(self):
            # TODO возвращаем ключ
            return self.key

        def get_value(self):
            # TODO возвращаем значение
            return self.value

        def __eq__(self, other):
            # TODO реализовать функцию сравнения
            return self.key == other.key

    def __init__(self, bucket_num=64):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''
        self.size = bucket_num
        self.loaded_buckets = 0
        self.count_entries = 0
        self.buckets = [[] for i in range(self.size)]

    def get(self, key, default_value=None):
        # TODO метод get, возвращающий значение,
        #  если оно присутствует, иначе default_value
        hash_key = self._get_hash(key)
        index = self._get_index(hash_key)
        element = self.Entry(key, None)

        for i in self.buckets[index]:
            if i == element:
                return i.value
        return default_value

    def put(self, key, value):
        # TODO метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        hash_key = self._get_hash(key)
        index = self._get_index(hash_key)
        element = self.Entry(key, value)

        if not self.buckets[index]:
            self.buckets[index] = [element]
            self.loaded_buckets += 1
            self.count_entries += 1
            # print(self.buckets)
            if self.loaded_buckets >= 2 / 3 * self.size:
                self._resize()

            return True

        flag = 0
        for i in self.buckets[index]:
            if i == element:
                self.buckets[index][self.buckets[index].index(i)].value = value
                # print (element.key,element.value,'azaz')
                flag = 1
        if flag == 0:
            self.buckets[index].append(element)
            self.count_entries += 1
            # print (self.count_entries)

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return self.count_entries

    def _get_hash(self, key):
        # TODO Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        return hash(key)

    def _get_index(self, hash_value):
        # TODO По значению хеша вернуть индекс элемента в массиве
        return hash_value % self.size

    def values(self):
        # TODO Должен возвращать итератор значений
        return ValuesIterator(self)

    def keys(self):
        # TODO Должен возвращать итератор ключей
        return KeysIterator(self)

    def items(self):
        # TODO Должен возвращать итератор пар ключ и значение (tuples)
        return ItemsIterator(self)

    def _resize(self):
        # TODO Время от времени нужно ресайзить нашу хешмапу
        # tmp = self.items()
        tmp = self.items()
        tmp_lst = []
        for item in tmp:
            tmp_lst.append((item[0], item[1]))

        self.size *= 2
        self.buckets = [[] for i in range(self.size)]
        self.loaded_buckets = 0
        self.count_entries = 0

        for item in tmp_lst:
            # print (item)
            self.put(item[0], item[1])

    def __str__(self):  # хз, что вы хотели, поэтому вывел это
        # TODO Метод выводит "buckets: {}, items: {}"
        return "buckets: {}, items: {}".format(self.loaded_buckets, self.count_entries)

    def __contains__(self, item):
        # TODO Метод проверяющий есть ли объект (через in)
        return item in self.keys()  # или айтемс ?


class KeysIterator():

    def __iter__(self):
        return self

    def __init__(self, hashmap):
        self.hashmap = hashmap
        self.num_of_bucket = 0
        self.num_of_entry = 0

    def __next__(self):
        while self.num_of_bucket < self.hashmap.size:
            while self.num_of_entry < len(self.hashmap.buckets[self.num_of_bucket]):
                self.num_of_entry += 1
                return self.hashmap.buckets[self.num_of_bucket][self.num_of_entry - 1].get_key()
            self.num_of_bucket += 1
            self.num_of_entry = 0
        raise StopIteration


class ValuesIterator():

    def __iter__(self):
        return self

    def __init__(self, hashmap):
        self.hashmap = hashmap
        self.num_of_bucket = 0
        self.num_of_entry = 0

    def __next__(self):
        while self.num_of_bucket < self.hashmap.size:
            while self.num_of_entry < len(self.hashmap.buckets[self.num_of_bucket]):
                self.num_of_entry += 1
                return self.hashmap.buckets[self.num_of_bucket][self.num_of_entry - 1].get_value()
            self.num_of_bucket += 1
            self.num_of_entry = 0
        raise StopIteration


class ItemsIterator():

    def __iter__(self):
        return self

    def __init__(self, hashmap):
        self.hashmap = hashmap
        self.num_of_bucket = 0
        self.num_of_entry = 0

    def __next__(self):
        while self.num_of_bucket < self.hashmap.size:
            while self.num_of_entry < len(self.hashmap.buckets[self.num_of_bucket]):
                self.num_of_entry += 1
                return (self.hashmap.buckets[self.num_of_bucket][self.num_of_entry - 1].get_key(),
                        self.hashmap.buckets[self.num_of_bucket][self.num_of_entry - 1].get_value())
            self.num_of_bucket += 1
            self.num_of_entry = 0
        raise StopIteration
