#Uses python3

import sys

def reach(adj, x, y,visited):
    visited[x] = True
    for i in range(len(adj[x])):
        w = adj[x][i]
        if not visited[w]:
            reach(adj,w, y,visited)
            if visited[y]:
                return 1
        
    return 0



if __name__ == '__main__':
    #edges =[]
    #f = open("02","r")
    #lines = f.readlines()
    #n, m = map(int,lines[0].split())
    #for i in range(1,m+1):
    #    edges.append((int(lines[i].split()[0]),int(lines[i].split()[1])))
    #x,y = map(int,lines[-1].split())

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[-2:]
    adj = [[] for _ in range(n)]
    visited = [False for _ in range(n)] 
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y,visited))
