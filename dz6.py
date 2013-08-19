#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Alex Dobrushskiy'

from collections import deque
import random
import csv
from datetime import datetime

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1

    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1

    return G


def read_graph(filename):
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    actors = {}
    movies = {}
    for (actor, movie_name, year) in tsv:
        movie = str(movie_name) + ", " + year
        actors[actor] = 1
        movies[movie] = 1
        make_link(G, actor, movie)

    return G, actors, movies


def centrality(G, v):
    distance_from_start = {}
    distance_from_start[v] = 0
    open_list = [v]
    while len(open_list) > 0:
        current = open_list.pop(0)
        for neightbor in G[current].keys():
            if neightbor not in distance_from_start:
                distance_from_start[neightbor] = distance_from_start[current] + 1
                open_list.append(neightbor)
    return (float(sum(distance_from_start.values())))/len(distance_from_start)


def rank(L, v):
    r = 0
    for l in L:
        if l < v:
            r += 1
    return r


def find_rank(L, i):
    lt = {}
    eq = {}
    gt = {}
    v = random.choice(L.keys())
    for l in L.keys():
        if L[l] < L[v]:
            lt[l] = L[l]
        elif L[l] == L[v]:
            eq[l] = L[l]
        elif L[l] > L[v]:
            gt[l] = L[l]
    if len(lt) >= i:
        return find_rank(lt, i)
    elif len(lt) + len(eq) >= i:
        return v
    else:
        return find_rank(gt, i - len(lt) - len(eq))


(G, actors, movies) = read_graph('file')
centralities = {}
lac = len(actors)
cnt = 1

start =  datetime.now()
for actor in actors.keys():
    print "Proccessed %d from %d" % (cnt, lac)
    centralities[actor] = centrality(G, actor)
    cnt += 1
actor_index = find_rank(centralities, 20)

print start
print datetime.now()
print actor_index
print centralities[actor_index]