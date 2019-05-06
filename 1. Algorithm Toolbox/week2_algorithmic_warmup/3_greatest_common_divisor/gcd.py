# Uses python3
import sys

def gcd(a, b):
    current_gcd = 1
    if b == 0:
        return a
    else:
        a_prime = a%b
        a = gcd(b,a_prime)
    
    return a

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
