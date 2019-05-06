# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    j=l
    i=j
    t=r
    m1=l
    m2=r
    while i<=t:
        if a[i] < x:
            a[i], a[j] = a[j], a[i]
            j+=1

        elif a[i] > x:      
            a[t],a[i] = a[i], a[t]
            t-=1
            i-=1
        i+=1
    m1 = j
    m2 = t

    return [m1,m2]
    

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #m = partition2(a, l, r)
    [m1, m2] = partition3(a,l,r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    #f = open("01","r")
    #lines = f.readlines()
    #n = int(lines[0])
    #a = list(map(int,lines[1].split()))
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
