#! /env/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Alex Dobrushskiy'


def right(i):
    return 2*i+2


def left(i):
    return 2*i+1


def parent(i):
    if i == 0:
        return 0
    return (i-1)/2


def up_heapify(heap, index):
    # if index == 0:
    #     return heap
    if heap[index][0] >= heap[parent(index)][0]:
        return heap
    else:
        heap[index], heap[parent(index)] = heap[parent(index)], heap[index]
        return up_heapify(heap, parent(index))


def down_heapify(heap, index):
    if left(index) > len(heap)-1:
        return heap
    if left(index) == len(heap)-1 and heap[index] <= heap[left(index)]:
        return heap
    elif left(index) == len(heap)-1 and heap[index] > heap[left(index)]:
        heap[index], heap[left(index)] = heap[left(index)], heap[index]
        return heap

    if heap[index][0] <= heap[left(index)][0] and heap[index][0] <= heap[right(index)][0]:
        return heap
    if heap[index][0] > heap[left(index)][0]:
        heap[index], heap[left(index)] = heap[left(index)], heap[index]
        return down_heapify(heap, left(index))
    if heap[index][0] > heap[right(index)][0]:
        heap[index], heap[right(index)] = heap[right(index)], heap[index]
        return down_heapify(heap, right(index))


def append_to_heap(heap, item):
    heap.append(item)
    return up_heapify(heap, len(heap)-1)


def make_heap(array):
    heap = []
    for i in array:
        append_to_heap(heap, i)
    return heap


def pop_heap(heap):
    if not heap:
        return None
    result = heap[0]
    heap[0] = heap[-1]
    del heap[-1]
    down_heapify(heap, 0)
    return result


def heap_replace(heap, index, elem):
    if heap[parent(index)][0] >= elem:
        heap[index] = elem
        up_heapify(heap, index)
    else:
        heap[index] = elem
        down_heapify(heap, index)