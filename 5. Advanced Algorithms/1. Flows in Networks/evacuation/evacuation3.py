# python3

from collections import deque

def max_flow(n,s,t,c):
    INF = float("Inf")
    max_flow = 0

    f = [[0 for k in range(n)] for i in range(n)]

    while True:
        prev = [-1 for _ in range(n)]
        prev[s] = -2
        q = deque()
        q.append(s)

        while q and prev[t]==-1:
            u = q.popleft()
            for v in range(n):
                cf =c[u][v] - f[u][v]
                if cf > 0 and prev[v]==-1:
                    q.append(v)
                    prev[v] = u

        if prev[t]==-1:
            break

        v = t
        delta = INF
        while True:
            u=prev[v]
            cf = c[u][v] - f[u][v]
            delta = min(delta, cf)
            v = u
            if v==s:
                break

        v = t
        while True:
            u = prev[v]
            f[u][v]+=delta
            f[v][u]-=delta
            v=u
            if v==s:
                break

        max_flow+=delta

    return max_flow

def read_data_test():
    lines = open("tests/02","r").readlines()
    vertex_count, edge_count = map(int, lines[0].split())
    capacity_matrix = [[0 for k in range(vertex_count)] for i in range(vertex_count)]
    for _ in range(1,edge_count+1):
        u, v, capacity = map(int, lines[_].split())
        capacity_matrix[u-1][v-1] = capacity_matrix[u-1][v-1]  + capacity
    return vertex_count, edge_count, capacity_matrix


def read_data():
    vertex_count, edge_count = map(int, input().split())
    capacity_matrix = [[0 for k in range(vertex_count)] for i in range(vertex_count)]
    for _ in range(1,edge_count+1):
        u, v, capacity = map(int, input().split())
        capacity_matrix[u-1][v-1] = capacity_matrix[u-1][v-1]  + capacity
    return vertex_count, edge_count, capacity_matrix
    
    return graph

if __name__ == '__main__':
    #graph = read_data()
    #vertex_count, edge_count, capacity_matrix = read_data()
    vertex_count, edge_count, capacity_matrix = read_data_test()
    flow = max_flow(vertex_count,0, vertex_count-1, capacity_matrix)
    print(flow)