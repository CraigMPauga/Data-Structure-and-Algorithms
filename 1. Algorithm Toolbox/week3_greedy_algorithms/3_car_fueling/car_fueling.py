# python3
import sys


def compute_min_refills(distance, tank, stops,num_stops):
    numRefills = 0
    currentRefill = 0
    stops = [0] + stops + [distance]
    while currentRefill <= num_stops:
        lastRefill = currentRefill
        while (currentRefill <= num_stops and ((stops[currentRefill+1] - stops[lastRefill]) <= m)):
            currentRefill = currentRefill + 1
        if currentRefill == lastRefill:
            return -1
        if currentRefill <= num_stops:
            numRefills+=1


    return numRefills

if __name__ == '__main__':

    #f = open("02","r")
    #lines = f.readlines()
    #d = int(lines[0])
    #m = int(lines[1])
    #num_stops = int(lines[2])
    #stops = list(map(int, lines[3].split()))
    d = int(input())
    m = int(input())
    num_stops = int(input())
    stops = list(map(int, sys.stdin.read().split()))
    
    print(compute_min_refills(d, m, stops,num_stops))
