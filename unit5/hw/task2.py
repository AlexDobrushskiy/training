#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Alex Dobrushskiy'

import re
from utils.dijkstra import dijkstra
from utils.paths import shortest_paths


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

if __name__ == '__main__':

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

    G = simple_G

    total_result = 0

    for i in search_list:
        dist = dijkstra(new_G, search_list[0])
        paths = shortest_paths(G, i)

        costed_paths = {}
        for j in paths:
            cost = 0
            for index in range(len(paths[j])-2):
                node1 = paths[j][index]
                node2 = paths[j][index+1]
                cost += new_G[node1][node2]
            costed_paths[j] = cost

        total_list = []
        for i in costed_paths.keys():
            if dist[i] != costed_paths[i]:
                total_list.append(i)

        print len(total_list)
        total_result += len(total_list)

    print total_result


####################################################################
#Let's calculate all shortest paths for current node

# Let make the path a list of nodes we need to visit, like that:
# ['A', 'D', 'F', 'G']  <--- from 'A' node to 'G' node

# So the result will be a dictionary with nodes as a keys
# And path-lists as a values, like so:
# {'A': ['A'], 'G' : ['A', 'D', 'F', 'G']}

# G is a graph
# v is a node to start from





