#!/usr/bin/env python
# coding: utf-8


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        # TODO: реализовать метод
        self.users = {}

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        # TODO: реализовать метод
        if user_id not in self.users:
            self.users[user_id] = [time]
        else:
            self.users[user_id].append(time)

    def query(self, count, time):
        """
        Этот метод отвечает на запросы.
        Возвращает количество пользователей, которые за последние 5 минут
        (на полуинтервале времени (time - 5 min, time]), совершили ровно count действий
        :param count: количество действий
        :param time: время для рассчета интервала
        :return: activity_count: int
        """
        # TODO: реализовать метод
        cnt = 0
        for user in self.users:
            tmp = 0
            if min(self.users[user]) > time:
                continue
            for timee in self.users[user]:
                if time - self.FIVE_MIN < timee <= time:
                    tmp += 1
            if tmp == count:
                cnt += 1
        return cnt
