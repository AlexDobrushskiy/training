#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Alex'

import re


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
print len(G)
print len(heroes), len(books)

new_G = {}

for node in G.keys():
    if node in heroes:
        for book in G[node]:
            for hero in G[book]:
                if node != hero:
                    make_link(new_G, node, hero)


print len(new_G)

max = 0
from_node = ""
to_node = ""

for node in new_G.keys():
    for link in new_G[node]:
        if (new_G[node])[link] > max:
            max = (new_G[node])[link]
            from_node = node
            to_node = link

print max, from_node, to_node
