#! /env/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Alex Dobrushskiy'

import heap_dict
from random import randint

# arr = [(randint(100, 200), randint(1, 50)) for i in range(20)]
#
# print arr
# heap = heap_dict.make_heap(arr)
# print heap
#
# print min(arr, key=lambda x: x[0]) # == heap[0]
# print heap[0]

#arr = [(174, 22), (186, 35), (168, 39), (136, 40), (120, 23), (197, 49), (189, 46), (102, 39), (139, 44), (163, 14)]
# arr = [(i, randint(30, 50)) for i in range(1,10)]
# arr.append((1, 'a'))
# heap_dict.up_heapify(arr, len(arr)-1)
# assert arr[1][1] == 'a'
# print arr
#
# arr = [(i, randint(30, 50)) for i in range(1,10)]
# print heap_dict.pop_heap(arr)
# print arr

arr = [(i, randint(30, 50)) for i in range(1,20)]
a = heap_dict.append_to_heap(arr, (-20, 'a'))
print a