# uses python3

BINARY = 2

def de_bruijn(k, n):

    binary_arr = ["0","1"]
    a = [0] * k * n
    sequence = []
    def db(t, p):
        if t > n:
            if n % p == 0:
                for j in range(1, p + 1):
                    sequence.append(a[j])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)
    db(1, 1)
    return "".join(binary_arr[i] for i in sequence)

if __name__ == "__main__":
    print(de_bruijn(BINARY, int(input())))