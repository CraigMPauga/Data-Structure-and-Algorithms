#Uses python3

import sys
import queue

def distance(adj, s, t):
    #Set the distance from the starting point to be zero
    ma = sys.maxsize
    dist =[ma for _ in range(n)]
    dist[s] = 0

    Q = queue.Queue()
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for i in range(len(adj[u])):
            v=adj[u][i]
            if dist[v]==ma:
                Q.put(v)
                dist[v] = dist[u]+1
    if dist[t]!=ma:
        return dist[t]
    else:
        return -1


if __name__ == '__main__':

    #edges =[]
    #f = open("02","r")
    #lines = f.readlines()
    #n, m = map(int,lines[0].split())
    #for i in range(1,m+1):
    #    edges.append((int(lines[i].split()[0]),int(lines[i].split()[1])))
    #s,t = map(int,lines[-1].split())
    #s,t = s-1,t-1

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1

    
    
    visited = [False for _ in range(n)]
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    
    print(distance(adj, s, t))
