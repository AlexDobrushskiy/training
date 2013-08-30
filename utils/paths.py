#! /env/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Alex Dobrushskiy'

from collections import deque


def shortest_paths(G, v):
    shortest_paths = {v: [v]}
    queue = deque([v])
    visited = []
    while len(queue) > 0:
        node = queue.popleft()
        visited.append(node)
        for i in G[node]:
            if i not in shortest_paths:
                shortest_paths[i] = shortest_paths[node] + [i]
            if i not in queue and i not in visited:
                queue.append(i)
    return shortest_paths
