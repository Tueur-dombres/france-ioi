from sys import setrecursionlimit

def dfs(node, parent, time):
    global i_prof, plus_bas, T_arcs
    time += 1
    i_prof[node] = time
    lowest_time = time
    for neighbor in adjacents[node]:
        if neighbor == parent:
            continue
        if i_prof[neighbor] == 0:
            T_arcs[node].append(neighbor)
            lowest_time_neighbor = dfs(neighbor, node, time)
            lowest_time = min(lowest_time, lowest_time_neighbor)
        else:
            lowest_time = min(lowest_time, i_prof[neighbor])
    plus_bas[node] = lowest_time
    return lowest_time

nbIntersections, nbSentiers = map(int, input().split())
setrecursionlimit(nbIntersections + 50)
adjacents = [[] for _ in range(nbIntersections)]
for _ in range(nbSentiers):
    n1, n2 = map(int, input().split())
    adjacents[n1 - 1].append(n2 - 1)
    adjacents[n2 - 1].append(n1 - 1)

i_prof = [0] * nbIntersections
plus_bas = [0] * nbIntersections
T_arcs = [[] for _ in range(nbIntersections)]

dfs(0, -1, 0)

isthmes = []
for x, ys in enumerate(T_arcs):
    for y in ys:
        if i_prof[x] < plus_bas[y]:
            isthmes.append(sorted([x + 1, y + 1]))

isthmes = sorted(isthmes)
print(len(isthmes))
for n1, n2 in isthmes:
    print(n1,n2)
