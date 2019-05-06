# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def min_optimal_sequence(n):
    sequence=[]
    minOp = [0]*(n+1)
   
    for i in range(n+1):
        minOp[i] = 0

    for num in range(2,n+1):

        sub_min = minOp[num-1]
        half_min = sys.maxsize
        third_min = sys.maxsize

        if num%2 == 0:
            half_min = minOp[num//2]
        if num%3 == 0:
            third_min = minOp[num//3]
        mini = min(sub_min, half_min, third_min)
        minOp[num] = mini + 1

    #backtrack
    x=n
    while x>=1:
        sub_min = minOp[x-1]
        half_min = sys.maxsize
        third_min = sys.maxsize
        sequence.insert(0,x)
        if x%2 == 0 and x%3==0:
            third_min =minOp[x//3]
        if x%3==0:
            third_min = minOp[x//3]
        if x%2==0:
            half_min = minOp[x//2]

        if third_min <= half_min and third_min <= sub_min:
            x=x//3
        if half_min <= sub_min and half_min < third_min:
            x=x//2
        if sub_min < half_min and sub_min < third_min:
            x=x-1
    return sequence

input = sys.stdin.read()
n = int(input)
sequence = list(min_optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
