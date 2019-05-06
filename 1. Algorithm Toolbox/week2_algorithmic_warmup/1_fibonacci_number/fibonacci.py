# Uses python3
def calc_fib(n):
    F = [None]*n
    if (n <= 1):
        return n
    else:
        F[0] = 0
        F[1] = 1
        i=2
        for i in range(2,n):
            F[i]= F[i-1] + F[i-2]
        fib = F[-1] + F[-2]

    return fib

n = int(input())
print(calc_fib(n))
