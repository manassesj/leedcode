from math import inf

vertices = 5

lista = [
        [[2, 1], [4, 2]],
        [[2, 0], [5, 3]],
        [[4, 0], [1, 3], [5, 4]],
        [[5, 1], [1, 2], [2, 4]],
        [[5, 2], [2, 3]]
    ]

s = 0

def menor(s):
    dist = [1e9] * vertices
    dist[0] = 0
    visi = [False] * vertices
    prio = []

    prio.append([0, 0])

    while len(prio) != 0:
        u = prio[0][1]
        prio.pop()
        if visi[u] == True:
            continue     
        visi[u] = True

        for n in lista[u]:
            v, w = n[1], n[0]

            if(dist[v] > dist[u] + w):
                dist[v] = dist[u] + w
                prio.insert(0, [dist[v], v])
    print(dist)

menor(s)





