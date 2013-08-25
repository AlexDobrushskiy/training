#
# The code below uses a linear
# scan to find the unfinished node
# with the smallest distance from
# the source.
#
# Modify it to use a heap instead
# 
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
    if heap[index][0] <= heap[left(index)][0] and heap[index][0] <= heap[right(index)][0]:
        return heap
    if heap[index][0] > heap[left(index)][0]:
        heap[index], heap[left(index)] = heap[left(index)], heap[index]
        return down_heapify(heap, left(index))
    if heap[index][0] > heap[right(index)][0]:
        heap[index], heap[right(index)] = heap[right(index)], heap[index]
        return down_heapify(heap, right(index))

def pop_heap(heap):
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


def shortest_dist_node(heap):
    return pop_heap(heap)[1]


def dijkstra(G, v):
    dist_so_far = {v: 0}
    heap = [(0, v)]
    final_dist = {}
    while len(final_dist) < len(G):
        w = shortest_dist_node(heap)
        # lock it down!
        final_dist[w] = dist_so_far[w]
        del dist_so_far[w]
        for x in G[w]:
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                    heap.append((dist_so_far[x], x))
                    up_heapify(heap, len(heap)-1)
                elif final_dist[w] + G[w][x] < dist_so_far[x]:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                    for i in range(len(heap)):
                        if heap[i][1] == x:
                            index = i
                            break
                    heap_replace(heap, index, (dist_so_far[x], x))
    return final_dist

############
# 
# Test

def make_link(G, node1, node2, w):
    if node1 not in G:
        G[node1] = {}
    if node2 not in G[node1]:
        (G[node1])[node2] = 0
    (G[node1])[node2] += w
    if node2 not in G:
        G[node2] = {}
    if node1 not in G[node2]:
        (G[node2])[node1] = 0
    (G[node2])[node1] += w
    return G


def test():
    # shortcuts
    (a,b,c,d,e,f,g) = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    triples = ((a,c,3),(c,b,10),(a,b,15),(d,b,9),(a,d,4),(d,f,7),(d,e,3), 
               (e,g,1),(e,f,5),(f,g,2),(b,f,1))
    G = {}
    for (i,j,k) in triples:
        make_link(G, i, j, k)

    dist = dijkstra(G, a)
    assert dist[g] == 8 #(a -> d -> e -> g)
    assert dist[b] == 11 #(a -> d -> e -> g -> f -> b)

test()
    




