# Uses python3
import sys

def fibonacci_sum(n):
    fib = 0
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    
            v1, v2, v3 = v1+v2, v1, v2
    if n == 0:
        fib = 0
    elif n == 1:
        fib == 1
    else:
        fib = v2
    return fib

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    i=0
    ans=0
    fib = 0

    while i<=n:
        ans = fibonacci_sum(i)
        fib = fib + ans
        i+=1
    print(fib)


