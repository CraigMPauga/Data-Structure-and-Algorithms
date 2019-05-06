# Uses python3
import math
import sys

def gcd(a, b):
    current_gcd = 1
    if b == 0:
        return a
    else:
        a_prime = a%b
        a = gcd(b,a_prime)
    
    return a

def lcm(a, b):
    greatcd = gcd(a,b)
    top = a * b
    ans = int(top//greatcd)
    #ans = int(int((a*b))  // int(gcd(a,b)))
    return ans

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

