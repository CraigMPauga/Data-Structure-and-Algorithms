# Uses python3
import sys

def optimal_weight(W, weights,n):
    # write your code here
    value = [[0 for x in range(W+1)] for y in range(n+1)] 

    for i in range(1,n+1):
        for w in range(1,W+1):
            value[i][w] = value[i-1][w]
            if weights[i-1] <= w:
                val = value[i-1][w - weights[i-1]] + weights[i-1]
                if value[i][w]<val:
                    value[i][w]=val
    return value[n][W]


if __name__ == '__main__':
    #f=open("01","r")
    #lines = f.readlines()
    #W,n = lines[0].split()
    #W = int(W)
    #n = int(n)
    #w = list(map(int, lines[1].split()))
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w,n))
