# Uses python3
import sys
from math import floor

def binary_search(a,low,high, key):
    if high < low:
        return -1
    mid = floor(low + ((high-low)/2))
    if key == a[mid]:
        return mid
    elif key < a[mid]:
        return binary_search(a,low,mid -1, key)
    else:
        return binary_search(a,mid+1,high,key)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    #f = open("01","r")
    #lines = f.readlines()
    #data = lines[0].split()
    #n = int(data[0])
    #a = list(map(int,data[1:]))
    #data2 = lines[1].split()
    #m = int(data2[0])
    #x = list(map(int,data2[1:]))
    #low = 0
    #high = len(a)-1
    #for key in x:
    #    print(binary_search(a,low,high,key), end = ' ')
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    low = 0
    high = len(a)-1
    for x in data[n + 2:]:
        print(binary_search(a,low, high, x), end = ' ')
