#Uses python3

import sys

def acyclic(adj,visited,v,on_stack):

    if v in on_stack:
        return True

    
    on_stack.append(v)
    
    for i in range(len(adj[v])):
        if not visited[v]:
            w = adj[v][i]        
            if acyclic(adj,visited,w,on_stack):
                return True
    visited[v] = True
    on_stack.remove(v)
    return False

 
def DFS(adj,ind,visited):
    on_stack = []
    
    for v in range(len(visited)):
        if not visited[v]:
            if acyclic(adj,visited,v,on_stack):
                return 1
            else:
                continue
    return 0

if __name__ == '__main__':

    #edges =[]
    #f = open("08","r")
    #lines = f.readlines()
    #n, m = map(int,lines[0].split())
    #for i in range(1,m+1):
    #    edges.append((int(lines[i].split()[0]),int(lines[i].split()[1])))
 
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    adj = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    CCnum = [0 for _ in range(n)]
 
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    print(DFS(adj,0,visited))
    #print(acyclic(adj,visited,0))
