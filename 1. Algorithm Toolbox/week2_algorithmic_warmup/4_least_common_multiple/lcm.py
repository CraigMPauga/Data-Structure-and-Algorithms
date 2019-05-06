# Uses python3
import sys

def lcm(a, b):
    ans = a*b / gcd(a,b)
    return ans

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

def gcd(a, b):
    current_gcd = 1
    if b == 0:
        return a
    else:
        a_prime = a%b
        a = gcd(b,a_prime)
    
    return a


