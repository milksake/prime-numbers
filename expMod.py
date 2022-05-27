def expMod(a, x, n):
    if x == 0:
        return 1
    elif x % 2 == 0:
        t = expMod(a, x / 2, n)
        return (t * t) % n
    else:
        t = expMod(a, x - 1, n)
        return (t * (a % n)) % n

if __name__ == "__main__":
    print(expMod(128, 129, 17))