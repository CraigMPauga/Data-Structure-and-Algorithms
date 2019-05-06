# python3

from collections import deque
import queue

class Edge:

    def __init__(self, u, v, lowerbound,capacity):
        self.u = u
        self.v = v
        self.lowerBound = lowerbound
        self.capacity = capacity
        self.diff = capacity - lowerbound
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n+2)]

        self.dv = [0] * (n+2)
        self.D = 0

    def add_edge(self, from_, to, lowerbound, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to,lowerbound, capacity)
        backward_edge = Edge(to, from_,0, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)
        self.dv[from_]+= lowerbound
        self.dv[to] -= lowerbound

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow
        self.edges[id].diff -= flow
        self.edges[id ^ 1].diff += flow


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)

    for _ in range(edge_count):
        u, v,lowerbound, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1,lowerbound, capacity)

    # update source and sink
    for v in range(vertex_count):
        if graph.dv[v] < 0:
            graph.add_edge(vertex_count, v, 0, -graph.dv[v])
        if graph.dv[v] > 0:
            graph.add_edge(v, vertex_count+1, 0, graph.dv[v])
            graph.D += graph.dv[v]
    return graph, vertex_count, edge_count

def read_data_test():
    lines = open("03","r").readlines()
    vertex_count, edge_count = map(int, lines[0].split())
    graph = FlowGraph(vertex_count)
    for i in range(1,edge_count+1):
        u, v, lowerbound, capacity = map(int, lines[i].split())
        graph.add_edge(u - 1, v - 1, lowerbound, capacity)

    for v in range(vertex_count):
        if graph.dv[v] < 0:
            graph.add_edge(vertex_count, v, 0, -graph.dv[v])
        if graph.dv[v] > 0:
            graph.add_edge(v, vertex_count+1, 0, graph.dv[v])
            graph.D += graph.dv[v]
    return graph, vertex_count, edge_count

def max_flow(graph, from_, to):
    flow = 0
    while True:
        isPath,path,maxFlow = bfs(graph,from_,to)
        if not isPath:
            return flow
        for id in path:
            graph.add_flow(id,maxFlow)
        flow+=maxFlow
    return flow


def bfs(graph,from_,to):
    maxFlow = float("Inf")
    INF = float("Inf")
    n = graph.size()
    isPath = False
    path = []
    prev = [(None,None)] * n
    dist = [float('inf')] * n
    dist[from_] = 0
    q= queue.Queue()
    q.put(from_)
    while not q.empty():
        currNode = q.get()
        for id in graph.get_ids(currNode):
            currEdge = graph.get_edge(id)
            if dist[currEdge.v] == INF and currEdge.diff > 0:
                dist[currEdge.v] = dist[currNode]+1
                prev[currEdge.v] = (currNode,id)
                q.put(currEdge.v)
                if currEdge.v == to:
                    while True:
                        path.insert(0,id)
                        currFlow = graph.get_edge(id).diff
                        maxFlow = min(currFlow,maxFlow)
                        if currNode == from_:
                            break
                        currNode, id = prev[currNode]
                    isPath = True
    return isPath, path, maxFlow

def getCirculation(graph,flow,edge_count):
    flow_arr = [0] * edge_count
    if flow!=graph.D:
        print("NO")
    else:
        for i in range(edge_count):
            currEdge = graph.edges[i*2]
            flow_arr[i] = currEdge.flow + currEdge.lowerBound
        print("YES")
        print("\n".join(map(str,flow_arr)))

if __name__ == '__main__':
    graph, vertex_count, edge_count = read_data()
    #graph, vertex_count, edge_count = read_data_test()
    flow = max_flow(graph,vertex_count,vertex_count+1)
    getCirculation(graph,flow,edge_count)