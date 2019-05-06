# python3

import itertools

def varnum(i, j):
    return n*i + j

def exactly_one_of(literals,clauses):
    clauses.append([l for l in literals])

    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])
    return clauses


def read_data():
    n, m = map(int, input().split())
    edges = [ list(map(int, input().split())) for i in range(m) ]
    return n,m,edges

def read_data_test():
    lines = open("01","r").readlines()
    edges=[]
    n,m =list(map(int, lines[0].split()))

    for i in range(1,m):
        edges += [list(map(int,lines[i].split()))]

    return n,m,edges

def printEquisatisfiableSatFormula(clauses,n):
    print(str(len(clauses)) + ' ' + str(n * int(n)) )

    for i in range(len(clauses)):
        clauses[i].append(0)
        print(' '.join(map(str, clauses[i])))

if __name__ == "__main__":
    n,m,edges=read_data()
    #n,m,edges=read_data_test()
    clauses = []
    p = range(1,n+1)
    adjacent = [[] for x in range(n)]
    
    for i,j in edges:
        adjacent[i-1].append(j-1)
        adjacent[j-1].append(i-1)

    for i in range(n):
        literals = [varnum(i, j) for j in p]
        clauses = exactly_one_of(literals,clauses)

    for j in p:
        literals = [varnum(i, j) for i in range(n)]
        clauses = exactly_one_of(literals,clauses)

    for j in p[:-1]:
        for i, vertex in enumerate(adjacent):
            literals= [varnum(n, j+1) for n in vertex]
            clauses.append([-varnum(i, j)] + literals)

    printEquisatisfiableSatFormula(clauses,n)