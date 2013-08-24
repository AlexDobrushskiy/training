#! /env/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Alex Dobrushskiy'


def right(i):
    return 2*i+2


def left(i):
    return 2*i+1


def parent(i):
    return (i-1)/2


def up_heapify(heap, index):
    if heap[index] >= heap[parent(index)]:
        return heap
    else:
        heap[index], heap[parent(index)] = heap[parent(index)], heap[index]
        return up_heapify(heap, parent(index))


def down_heapify(heap, index):
    if left(index) > len(heap)-1:
        return heap
    if left(index) == len(heap)-1 and heap[index] <= heap[left(index)]:
        return heap
    if heap[index] <= heap[left(index)] and heap[index] <= heap[left(right)]:
        return heap
    if heap[index] > heap[left(index)]:
        heap[index], heap[left(index)] = heap[left(index)], heap[index]
        return down_heapify(heap, left(index))
    if heap[index] > heap[right(index)]:
        heap[index], heap[right(index)] = heap[right(index)], heap[index]
        return down_heapify(heap, right(index))


def make_heap(array):
    heap = []
    for i in array:
        heap.append(i)
        up_heapify(heap, len(heap)-1)
    return heap


def pop_heap(heap):
    result = heap[0]
    heap[0] = heap[-1]
    del heap[-1]
    down_heapify(heap, 0)
    return result
