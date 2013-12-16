#
# In lecture, we took the bipartite Marvel graph,
# where edges went between characters and the comics
# books they appeared in, and created a weighted graph
# with edges between characters where the weight was the
# number of comic books in which they both appeared.
#
# In this assignment, determine the weights between
# comic book characters by giving the probability
# that a randomly chosen comic book containing one of
# the characters will also contain the other
#

# from marvel import marvel, characters
def get_books_list(bipartiteG, characters):
    books = []
    for key in bipartiteG:
        if key not in characters:
            books.append(key)
    return books


def calc_prob(bipartiteG, books, a, b):
    # books = get_books_list(bipartiteG, characters)
    books_total = 0.
    books_both = 0.
    for book in books:
        if a in bipartiteG[book] or b in bipartiteG[book]:
            books_total += 1
        if a in bipartiteG[book] and b in bipartiteG[book]:
          books_both += 1
    if not books_both:
        return None
    return books_both/books_total


def create_weighted_graph(bipartiteG, characters):
    books = get_books_list(bipartiteG, characters)
    G = {}
    for i in characters:
        G[i] = {}

    for charA in characters:
        for charB in characters:
            if charA != charB:
                prob = calc_prob(bipartiteG, books, charA, charB)
                G[charA][charB] = prob
                G[charB][charA] = prob
    return G

######
#
# Test

def test():
    bipartiteG = {'charA':{'comicB':1, 'comicC':1},
                  'charB':{'comicB':1, 'comicD':1},
                  'charC':{'comicD':1},
                  'comicB':{'charA':1, 'charB':1},
                  'comicC':{'charA':1},
                  'comicD': {'charC':1, 'charB':1}}
    G = create_weighted_graph(bipartiteG, ['charA', 'charB', 'charC'])
    # three comics contain charA or charB
    # charA and charB are together in one of them
    assert G['charA']['charB'] == 1.0 / 3
    assert G['charA'].get('charA') == None
    assert G['charA'].get('charC') == None

# def test2():
#     G = create_weighted_graph(marvel, characters)
    
test()