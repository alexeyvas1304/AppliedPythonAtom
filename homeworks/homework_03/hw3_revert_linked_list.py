#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """
    # TODO: реализовать функцию
    tail = None
    while head:
        tmp = head.next_node
        head.next_node = tail
        tail = head
        head = tmp
    return tail
