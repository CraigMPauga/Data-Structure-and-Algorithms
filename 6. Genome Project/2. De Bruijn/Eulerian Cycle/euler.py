#uses python3
 
def readData():
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    return n,m,edges

def readDataTest():
    lines = open("03","r").readlines()
    n,m = map(int,(lines[0].split()))
    edges = []
    for i in range(1,m+1):
        edges.append(list(map(int,lines[i].split())))
    return n,m,edges

def adj_deg(n,m,edges):
    adj = [[] for _ in range(n)]
    edge_id = 0
    for (a, b) in edges:
        adj[a - 1].append(((b - 1), edge_id))
        edge_id += 1

    degree = [0]*n
    for s, e in edges:
        degree[s-1]+=1
        degree[e-1]-=1
    return adj,degree

def findCycle(adj,degee,start_node):
    if any(degree):
        print(0)
        return

    visited = set()
    path = [int(start_node)]
    node = int(start_node)
    while len(edges)>len(visited):
        for ind,node in enumerate(path):
            cycleCompleted = True
            for adjacent in adj[node]:
                if adjacent[1] not in visited:
                    cycleCompleted = False
                    break
            if cycleCompleted:
                continue
            next_cycle = [node]
            current = node
            nextCycle = True
            while nextCycle:
                nextCycle = False
                for next in adj[current]:
                    if next[1] not in visited:
                        visited.add(next[1])
                        next_cycle.append(int(next[0]))
                        current = next[0]
                        nextCycle=True
                        break
            break
        path = path[:ind]+next_cycle+path[ind+1:]
    path = list(map(lambda z: str(z+1), path))[:-1]
    print(1)
    print(" ".join(path))



if __name__ == '__main__':
    #n,m,edges =readDataTest()
    n,m,edges = readData()
    adj,degree = adj_deg(n,m,edges)
    findCycle(adj,degree,0)