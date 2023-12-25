#Uses python3

import sys


def neg_cycle(x, shortest, adj):
    shortest[x] = 0
    for i in adj[x]:
        if shortest[i] == 1:
            neg_cycle(i, shortest, adj)



def shortet_paths(n, adj, cost, s, distance, reachable, shortest):
    distance[s] = 0
    reachable[s] = 1
    for _ in range(n - 1):
        change = 0
        for i in range(n):
            if reachable[i] == 1:
                for k in range(len(adj[i])):
                    if reachable[adj[i][k]] == 0:
                        reachable[adj[i][k]] = 1
                        distance[adj[i][k]] = distance[i] + cost[i][k]
                        change += 1
                    else:
                        distance[adj[i][k]] = min(distance[i] + cost[i][k], distance[adj[i][k]])
                        change += 1
        if change == 0:
            break

    for i in range(n):
        if reachable[i] == 1:
            for k in range(len(adj[i])):
                if distance[i] + cost[i][k] < distance[adj[i][k]]:
                    distance[adj[i][k]] = distance[i] + cost[i][k]
                    if shortest[adj[i][k]] == 1:
                        shortest[adj[i][k]] = 0

    for i in range(n):
        if shortest[i] == 0:
            for x in adj[i]:
                if shortest[x] == 1:
                    neg_cycle(x, shortest, adj)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [(None)] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(n, adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])