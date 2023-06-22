def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(m * m):
        previous, current = current, (current + previous) % m # current will have the last digit
        if (previous == 0 and current == 1):
            pisanoPeriod = i + 1
            return pisanoPeriod


def fibonacci_huge_naive(n, m):
    
    # Getting the period and taking the mod
    n = n % pisanoPeriod(m)
    previous, current = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(n-1):
            previous, current = current, (previous+current) % m
        return current
    

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
