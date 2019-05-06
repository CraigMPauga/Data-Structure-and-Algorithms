# python3

import itertools

global num_colors

def varnum(i, j):
    return num_colors * (i-1) + j

def exactly_one_of(literals,clauses):
    clauses.append([l for l in literals])

    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])
    return clauses

def adj(i, j):
    for c in colors:
        clauses.append([-varnum(i, c), -varnum(j, c)])

def read_data():
    n, m = map(int, input().split())
    edges = [ list(map(int, input().split())) for i in range(m) ]
    return n,m,edges

def read_data_test():
    lines = open("01","r").readlines()
    edges=[]
    n,m =list(map(int, lines[0].split()))

    for i in range(1,n+1):
        edges += [list(map(int,lines[i].split()))]

    return n,m,edges

def printEquisatisfiableSatFormula(clauses,n,colors):
    print(str(len(clauses)) + ' ' + str(n * int(num_colors)) )

    for i in range(len(clauses)):
        clauses[i].append(0)
        print(' '.join(map(str, clauses[i])))

if __name__ == "__main__":
    n,m,edges=read_data()
    #n,m,edges=read_data_test()
    clauses = []
    colors = range(1,4)
    num_colors=3

    for i in range(1,n+1):
        literals = [varnum(i,c) for c in colors]
        clauses = exactly_one_of(literals,clauses)

    for i, j in edges:
        adj(i, j)

    printEquisatisfiableSatFormula(clauses,n,colors)




