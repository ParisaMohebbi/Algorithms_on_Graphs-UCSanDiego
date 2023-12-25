#import sys
#from collections import deque
#
#def bipartite(adj, n, k):
#    colors = [-1] * n
#    for i in range(n):
#        if colors[i] == -1:
#            if not is_bipartite_bfs(adj, n, i, colors, k):
#                return 0  # Not k-partite
#    return 1  # Graph is k-partite
#
#def is_bipartite_bfs(adj, n, start, colors, k):
#    q = deque()
#    q.append(start)
#    colors[start] = 0
#
#    while q:
#        u = q.popleft()
#
#        for v in adj[u]:
#            if colors[v] == -1:
#                colors[v] = 1 - colors[u]
#                q.append(v)
#            elif colors[v] == colors[u]:
#                return False  # Graph is not bipartite
#
#    return True
#
#if __name__ == '__main__':
#    input_data = sys.stdin.read()
#    data = list(map(int, input_data.split()))
#    n, m, k = data[0:3]
#    data = data[3:]
#    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
#    adj = [[] for _ in range(n)]
#
#    for (a, b) in edges:
#        adj[a - 1].append(b - 1)
#        adj[b - 1].append(a - 1)
#
#    print(bipartite(adj, n, k))


# Uses python3

import sys
import queue

def bipartite(adj):
    visited = [False] * len(adj)
    visited[0] = True

    partition = [-1] * len(adj)
    partition[0] = 0

    queue = []
    queue.append(0)

    while queue:
        v = queue.pop(0)
        for u in adj[v]:
            if partition[u] == partition[v]:
                return 0
            else:
                if not visited[u]:
                    visited[u] = True
                    partition[u] = 1 - partition[v]
                    queue.append(u)

    return 1


if __name__ == '__main__':
    user_input = sys.stdin.read()
    data = list(map(int, user_input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))