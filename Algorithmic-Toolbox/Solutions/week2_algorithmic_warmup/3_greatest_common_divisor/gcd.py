def gcd(a, b):
    if a == b  or b == 0:
        return a
    elif b == 1:
        return 1
    else:
        a, b = b, a % b
        return gcd(a,b)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
