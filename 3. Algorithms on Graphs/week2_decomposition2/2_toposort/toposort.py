#Uses python3

import sys

def topsort(adj,visited,v,on_stack,used,post_order,used_ind):

    for i in range(len(adj[v])):
        if not visited[v]:
            w = adj[v][i]        
            if topsort(adj,visited,w,on_stack,used,post_order,used_ind):
                return True

    if visited[v]==False:
        used_ind.append(v)

    visited[v] = True
    

 
def DFS(adj,visited,used,post_order,used_ind):
    on_stack = []
    order=[]
   
    for v in range(len(visited)):
        if not visited[v]:
            topsort(adj,visited,v,on_stack,used,post_order,used_ind)


    return used_ind

if __name__ == '__main__':

    #edges =[]
    #f = open("04","r")
    #lines = f.readlines()
    #n, m = map(int,lines[0].split())
    #for i in range(1,m+1):
    #    edges.append((int(lines[i].split()[0]),int(lines[i].split()[1])))

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    post_order=0
    used =[0 for _ in range(n)]
    used_ind =[]
    visited = [False for _ in range(n)]
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    order = DFS(adj,visited,used,post_order,used_ind)
    for x in reversed(order):
        print(x+1, end=' ')

