# Uses python3
import sys
import itertools

def partition3(A,n):
    sum = 0

    for x in range(n):
        sum+=A[x]

    if sum%3!=0:
        return 0

    part = [[0 for x in range(n+1)] for y in range(sum//3 + 1)]


    for i in range(1,(sum//3)+1):
        for j in range(1,n+1):
            if A[j-1] == i or ((i-A[j-1]) and part[i-A[j-1]][j-1]):


if __name__ == '__main__':
    f=open("01","r")
    lines = f.readlines()
    n = int(lines[0])
    A = list(map(int,lines[1].split()))
    #input = sys.stdin.read()
    #n, *A = list(map(int, input.split()))
    print(partition3(A,n))

