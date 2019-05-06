#Uses python3

import sys


def negative_cycle(adj, cost,visited):
    #write your code here
    ma = sys.maxsize
    dist = [ma for _ in range(n)]
    prev = [None for _ in range(n)]
    u=0
    dist[u]=0
    for _ in range(n):
        for u in range(n):
            for i in range(len(adj[u])):
                #relax edge
                v=adj[u][i]
                if dist[v] > dist[u] + cost[u][i]:
                    dist[v] = dist[u] + cost[u][i]
                    prev[v] = u

    for u in range(n):
        for i in range(len(adj[u])):
            #relax edge
            v=adj[u][i]
            if dist[v] > dist[u] + cost[u][i] and dist[v]<ma:
                return 1
        visited[u] = True
    return 0



if __name__ == '__main__':

    #edges =[]
    #f = open("01","r")
    #lines = f.readlines()
    #n, m = map(int,lines[0].split())
    #for i in range(1,m+1):
    #    a,b,w=int(lines[i].split()[0]),int(lines[i].split()[1]),int(lines[i].split()[2])
    #    c=((a,b),w)
    #    edges.append(c)

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]

    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost, visited))
