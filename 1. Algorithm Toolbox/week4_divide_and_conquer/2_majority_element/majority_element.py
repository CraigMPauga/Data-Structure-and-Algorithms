# Uses python3
import sys
from math import ceil
def get_majority_element(a):
    if len(a) == 0:
        return 1
    if len(a) == 1:
        return a[0]

    mid = len(a)//2

    low = get_majority_element(a[0:mid])
    high = get_majority_element(a[mid:])

    if low == high:
        return low
    if a.count(low) > mid:
        return low
    if a.count(high) > mid:
        return high
    return -1


if __name__ == '__main__':
    #f = open("01","r")
    #lines = f.readlines()
    #n = int(lines[0])
    #a = list(map(int,lines[1].split()))
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)
