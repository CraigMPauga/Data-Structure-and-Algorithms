#Uses python3

import sys
from queue import PriorityQueue 

def distance(adj, cost, s, t):
    #setup infinite and dist arrayu
    ma = sys.maxsize
    dist = [ma for _ in range(n)]
    prev = [None for _ in range(n)]
    dist[s] = 0

    #create priority queue with distance values as the keyss
    H = PriorityQueue()
    H.put(s,dist[s])
    while not H.empty():
        u = H.get()
        for i in range(len(adj[u])):
            v = adj[u][i]
            if dist[v]> dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                prev[v] = u
                H.put(v,dist[v])
            
    if dist[t]==ma:
        return -1
    else:
        return dist[t]


if __name__ == '__main__':

    #edges =[]
    #f = open("03","r")
    #lines = f.readlines()
    #n, m = map(int,lines[0].split())
    #for i in range(1,m+1):
    #    a,b,w=int(lines[i].split()[0]),int(lines[i].split()[1]),int(lines[i].split()[2])
    #    c=((a,b),w)
    #    edges.append(c)
    #s,t = map(int,lines[-1].split())
    #s,t = s-1,t-1

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    s, t = data[0] - 1, data[1] - 1

    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    
    print(distance(adj, cost, s, t))
