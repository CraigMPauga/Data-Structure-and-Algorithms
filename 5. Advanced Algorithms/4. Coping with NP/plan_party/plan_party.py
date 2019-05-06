#uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []


def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree
def ReadTreeTest():
    lines = open("03","r").readlines()
    size = int(lines[0])
    tree = [Vertex(w) for w in map(int, lines[1].split())]
    for i in range(2, size+1):
        a, b = list(map(int, lines[i].split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def dfs(tree, vertex, parent,D):
    if D[vertex]==None:
        if len(tree[vertex].children) == 1 and vertex !=0:
            D[vertex] = tree[vertex].weight
        else:
            m1 = tree[vertex].weight
            for u in tree[vertex].children:
                if u !=parent:
                    for w in tree[u].children:
                        if w!=vertex:
                            m1+=dfs(tree,w,u,D)
            m0=0

            for u in tree[vertex].children:
                if u!=parent:
                    m0+=dfs(tree,u,vertex,D)
            D[vertex] = max(m1,m0)
    maxFun = D[vertex]
    return maxFun

    # This is a template function for processing a tree using depth-first search.
    # Write your code here.
    # You may need to add more parameters to this function for child processing.


def MaxWeightIndependentTreeSubset(tree):
    weight = 0
    size = len(tree)
    if size == 0:
        return 0
    D=[None] * size
    maxFun = dfs(tree, 0, -1,D)
    # You must decide what to return.
    return maxFun


def main():
    tree = ReadTree();
    #tree = ReadTreeTest()
    weight = MaxWeightIndependentTreeSubset(tree);
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()
