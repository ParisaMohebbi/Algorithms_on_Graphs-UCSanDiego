#Uses python3

import sys

class queue:
    def __init__(self):
        self.q = []
        self.dist = [(-1)for _ in range(n)]

    def sort(self, value):
        k = 0
        for i in range(0, len(self.q)):
            if self.q[i] == value:
                k = i
                break
        for j in range(k, len(self.q) - 1):
            if self.dist[self.q[j]] >= self.dist[self.q[j+1]]:
                break
            else:
                self.q[j], self.q[j+1] = self.q[j+1], self.q[j]

    def put(self, value):
        if len(self.q):
            for i in range(0, len(self.q)):
                if self.dist[self.q[i]] < self.dist[value]:
                    self.q.insert(i, value)
                    break
                elif i == len(self.q) - 1:
                    self.q.append(value)
        else:
            self.q.append(value)

def distance(n, adj, cost, s, t):
    que = queue()
    que.dist[s] = 0
    que.put(s)
    while len(que.q):
        x = que.q.pop()
        for i in range(len(adj[x])):
            if que.dist[adj[x][i]] == -1:
                que.dist[adj[x][i]] = que.dist[x] + cost[x][i]
                que.put(adj[x][i])
            else:
                if que.dist[x] + cost[x][i] < que.dist[adj[x][i]]:
                    que.dist[adj[x][i]] = que.dist[x] + cost[x][i]
                    que.sort(adj[x][i])

    return que.dist[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(n, adj, cost, s, t))