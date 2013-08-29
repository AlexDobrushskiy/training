#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Alex Dobrushskiy'

import re
from utils.dijkstra import dijkstra


def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = G[node1].get(node2, 0) + 1

    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = G[node2].get(node1, 0) + 1

    return G


def read_graph(filename):
    tsv = open(filename)
    G = {}
    heroes = {}
    books = {}
    for line in tsv:
        elems = re.findall(r'\"(.+?)\"', line)
        hero, book = elems[0], elems[1]
        heroes[hero] = 1
        books[book] = 1
        make_link(G, hero, book)

    return G, heroes, books

G, heroes, books = read_graph('marvel')

new_G = {}

for node in G.keys():
    if node in heroes:
        for book in G[node]:
            for hero in G[book]:
                if node != hero:
                    make_link(new_G, node, hero)


print len(new_G)
# let simple_G be the unweighted graph
simple_G = new_G

for i in new_G:
    for j in new_G[i]:
        new_G[i][j] = 1./new_G[i][j]
print len(new_G)
# Now new_G is weighted graph. The smallest weight means the minimum cost of path

search_list = ['SPIDER-MAN/PETER PAR',
               'GREEN GOBLIN/NORMAN ',
               'WOLVERINE/LOGAN ',
               'PROFESSOR X/CHARLES ',
               'CAPTAIN AMERICA']

dist = dijkstra(new_G, search_list[0])