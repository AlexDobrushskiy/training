#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Alex Dobrushskiy'

from collections import deque

f = open('file')

actors = []
for line in f:
    words = line.split('\t')
    actors.append((words[0], words[1], words[2].strip()))

G = {}


def make_link(G, node1, node2):
    if node1 == node2:
        return

    if node1 in G:
        if node2 not in G[node1]:
            G[node1].append(node2)
    else:
        G[node1] = [node2]

    if node2 in G:
        if node1 not in G[node2]:
            G[node2].append(node1)
    else:
        G[node2] = [node1]


def distance(G, item):
    to_visit = deque([item])
    dist = {item: 0}
    while to_visit:
        current = to_visit.popleft()
        for neightbor in G[current]:
            if not neightbor in dist:
                dist[neightbor] = dist[current] + 1
                to_visit.append(neightbor)
    return dist


def avg_distance(G, item):
    to_visit = deque([item])
    dist = {item: 0}
    result = 0
    cnt = 1
    while to_visit:
        current = to_visit.popleft()
        for neightbor in G[current]:
            if not neightbor in dist:
                dist[neightbor] = dist[current] + 1
                result += dist[neightbor]
                to_visit.append(neightbor)
                cnt += 1
    return result*1.0/cnt

for item in actors:
    make_link(G, item[0], item[1])

new_G = {}

for actor, film, date in actors:
    if actor not in new_G:
        for film in G[actor]:
            for act in G[film]:
                make_link(new_G, actor, act)

avg_dst = []
cnt = 1
len_G = len(new_G)

for i in new_G:
    print "Processing %d of %d" % (cnt, len_G)
    avg_dst.append([i, avg_distance(new_G, i)])
    cnt += 1

sortedlist = sorted(avg_dst, key=lambda x: x[1])

print sortedlist[:20]
print sortedlist[0]
print sortedlist[19]
# print avg_distance(G, 'McClure, Marc (I)')
# print len(distance(G, 'McClure, Marc (I)'))
# print len(actors)
# print len(G)
# print actors[0]