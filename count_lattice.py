def sigma_odd(n):
    s = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            if d % 2:
                s += d
            o = n // d
            if o != d and o % 2:
                s += o
        d += 1
    return s

def C(X):
    return 1 + sum(24 * sigma_odd(m) for m in range(1, X + 1))

if __name__ == "__main__":
    for X in (40, 100, 150, 300, 2000):
        tot = C(X)
        print(f"N <= {X:4d}:  C(X) = {tot:9d}   targets 2..X = {tot - 1 - 24:9d}")
