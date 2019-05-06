#Uses python3
import sys
import math
from queue import PriorityQueue

class Point():
    def __init__(self, x,y,ID):
        self.x=x
        self.y=y
        self.ID = ID
        self.set = set()
        self.set.add(ID)
        
def calcDist(x1,y1,x2,y2):
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return dist

def minimum_distance(x, y):
    result = 0.
    ma = sys.maxsize
    points=[]
    E=[]
    X=[]

    for i in range(len(x)):
        points.append(Point(x[i],y[i],i))
    for i in range(n):
        for j in range(i+1,n):
            E.append([calcDist(x[i],y[i],x[j],y[j]),points[i].ID,points[j].ID])

    E.sort(key=lambda x: x[0])
    
    for e in E:
        if len(points[e[1]].set)==len(x):
            return result
        if points[e[1]].ID not in points[e[2]].set and points[e[2]].ID not in points[e[1]].set:

            src_set = points[e[1]].set
            dest_set = points[e[2]].set
            joined_set = set.union(src_set,dest_set)
            if set.isdisjoint(src_set,dest_set):
                result= result + e[0]
                for s in joined_set:
                    points[s].set = joined_set

    return result


if __name__ == '__main__':
    #x=[]
    #y=[]
    #f = open("02","r")
    #lines = f.readlines()
    #n = int(lines[0])
    #for i in range(1,n+1):
    #    x.append(int(lines[i].split()[0]))
    #    y.append(int(lines[i].split()[1]))

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
