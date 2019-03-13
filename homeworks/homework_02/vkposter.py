#!/usr/bin/env python
# coding: utf-8


# from homeworks.homework_02.heap import MaxHeap
# from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.user_subsc = {}
        self.user_posts = {}
        self.read_posts = {}

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if user_id not in self.user_posts:
            self.user_posts[user_id] = [post_id]
        else:
            self.user_posts[user_id].append(post_id)

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id not in self.read_posts:
            self.read_posts[post_id] = [1, [user_id]]
        elif post_id in self.read_posts and user_id \
                not in self.read_posts[post_id][1]:
            self.read_posts[post_id][0] += 1
            self.read_posts[post_id][1].append(user_id)

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if follower_user_id not in self.user_subsc:
            self.user_subsc[follower_user_id] = [followee_user_id]
        else:
            self.user_subsc[follower_user_id].append(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int) -> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        lst = []
        if user_id not in self.user_subsc:
            return lst
        for subscriber in self.user_subsc[user_id]:
            if subscriber in self.user_posts:
                lst += self.user_posts[subscriber]
                lst = sorted(lst, reverse=True)
        return lst[0:k]

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за
        все время,остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        lst = []
        sorted_by_count = sorted(self.read_posts.items(),
                                 key=lambda kv: (kv[1][0], kv[0]))
        sorted_by_count.reverse()
        for i in range(k):
            lst.append(sorted_by_count[i][0])
        return lst
