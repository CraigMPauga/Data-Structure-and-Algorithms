# python3

import threading

f = 1     
r = -1  
nontree = 0  

def nodeInd(i):

    if i> 0:
        node = 2*abs(i) - 2
    else:
        node = 2*abs(i) - 1
    return node

def posOrNeg(k):
    if 0 == 1 & k:
        return k//2+1
    else:
        return -k//2

def constructGraph(graph, graph_rev,clauses):
    for clause in clauses:
        graph[nodeInd(-clause[0])].append(nodeInd(clause[1]))
        graph[nodeInd(-clause[1])].append(nodeInd(clause[0]))

        graph_rev[nodeInd(clause[1])].append(nodeInd(-clause[0]))
        graph_rev[nodeInd(clause[0])].append(nodeInd(-clause[1]))
    return graph,graph_rev

def search(graph):
 
    visited = set()
    
    for v in range(len(graph)):
        if v not in visited:
            yield v,v,f
            visited.add(v)
            stack = [(v,iter(graph[v]))]
            while stack:
                parent,children = stack[-1]
                try:
                    child = next(children)
                    if child in visited:
                        yield parent,child,nontree
                    else:
                        yield parent,child,f
                        visited.add(child)
                        stack.append((child,iter(graph[child])))
                except StopIteration:
                    stack.pop()
                    if stack:
                        yield stack[-1][0],parent,r
            yield v,v,r

def postorder(graph):
    for v,w,edgetype in search(graph):
        if edgetype is r:
            yield w


def findSCCs(graph, graph_rev):
    post = list(postorder(graph_rev))
    reversePost = post[::-1]
    
    visited = [False] * len(graph)
    sccs = []
    sccsIndex = [0] * len(graph)
    currIndex = 0
    for v in reversePost:
        scc = set()
        if not visited[v]:
            S = []
            S.append(v)
            while len(S) > 0:
                v = S.pop()
                if not visited[v]:
                    visited[v] = True
                    scc.add(v)
                    sccsIndex[v] = currIndex
                    for w in graph[v]:
                        S.append(w)
            sccs.append(scc)

            currIndex += 1

    return sccs, sccsIndex

def checkSatisfication(sccs):
    for scc in sccs:
        for v in scc:
            if nodeInd(-posOrNeg(v)) in scc:
                return False
    return True

def isSatisfiable(n,m,clauses):
    graph = [[] for _ in range(2*n)]
    graph_rev = [[] for _ in range(2*n)]
    graph,GR = constructGraph(graph, graph_rev,clauses)
    sccs, sccsIndex = findSCCs(graph, graph_rev)
    if not checkSatisfication(sccs):
        return None

    result = [False] * n
    assigned = [False] * len(graph)
    post = postorder(graph)
    for v in post:
        if not assigned[v]:
            for w in sccs[sccsIndex[v]]:
                if not assigned[w]:
                    result[abs(posOrNeg(w))-1] = (posOrNeg(w) < 0)
                    assigned[w] = True
                    assigned[nodeInd(-posOrNeg(w))] = True
    return result


def read_data():
    n, m = map(int, input().split())
    clauses = [ list(map(int, input().split())) for i in range(m) ]
    return n,m,clauses

def read_data_test():
    lines = open("01","r").readlines()
    n,m = list(map(int, lines[0].split()))
    clauses=[]
    for i in range(1,m+1):
        clauses.append(list(map(int,lines[i].split())))
    return n,m,clauses

def circuit():
    n, m, clauses = read_data()
    #n,m, clauses = read_data_test()

    result = isSatisfiable(n,m,clauses)
    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE");
        print(" ".join(str(-i-1 if result[i] else i+1) for i in range(n)))

if __name__ == '__main__':
    threading.Thread(target=circuit).start()