#! /env/bin/python
# -*- coding: utf-8 -*-

from utils import heap_dict


def shortest_dist_node(heap):
    return heap_dict.pop_heap(heap)[1]


def dijkstra(G, v):
    dist_so_far = {v: 0}
    heap = [(0, v)]
    final_dist = {}
    while len(heap) > 0:
        w = shortest_dist_node(heap)

        # lock it down!
        final_dist[w] = dist_so_far[w]
        del dist_so_far[w]
        for x in G[w]:
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                    heap.append((dist_so_far[x], x))
                    heap_dict.up_heapify(heap, len(heap)-1)
                elif final_dist[w] + G[w][x] < dist_so_far[x]:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                    for i in range(len(heap)):
                        if heap[i][1] == x:
                            index = i
                            break
                    heap_dict.heap_replace(heap, index, (dist_so_far[x], x))
    return final_dist

