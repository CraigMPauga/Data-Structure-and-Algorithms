#Uses python3

import sys


def number_of_components(adj,x,visited,CCnum,cc):
    visited[x] = True
    CCnum[x] = cc 
    for i in range(len(adj[x])):
        w = adj[x][i]
        if not visited[w]:
            number_of_components(adj,w,visited,CCnum,cc)
    return CCnum

def DFS(adj,x,visited,CCnum,cc):
    cc=1
    for v in visited:
        if not v:
            number_of_components(adj,x,visited,CCnum,cc)
            cc+=1
    return max(CCnum)

if __name__ == '__main__':

    #edges =[]
    #f = open("01","r")
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
    adj = [[] for _ in range(n)]
    visited = [False for _ in range(n)] 
    CCnum = [0 for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(DFS(adj,0,visited,CCnum,1))
    #print(number_of_components(adj,0,visited,CCnum,1))
