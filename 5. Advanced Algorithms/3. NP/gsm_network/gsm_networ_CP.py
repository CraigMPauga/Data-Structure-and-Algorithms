#python 3


def SAT(n,m,edges,colors):

    C, V, cnt = K*len(edges) + n, n*K, 1
    print("{0} {1}".format(C, V))

    for i in range(1, n+1):
        print("{0} {1} {2} 0".format(cnt, cnt+1, cnt+2))
        cnt += 3

    for edge in edges:
        print("{0} {1} 0".format(-((edge[0]-1)*K+1), -((edge[1]-1)*K+1)))
        print("{0} {1} 0".format(-((edge[0]-1)*K+2), -((edge[1]-1)*K+2)))
        print("{0} {1} 0".format(-((edge[0]-1)*K+3), -((edge[1]-1)*K+3)))


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

print_SAT_formula()
if __name__ == "__main__":
    #n,m,edges=read_data()
    n,m,edges=read_data_test()
    colors = range(1,4)
    C,V,j = SAT(e,m,edges,colors)
