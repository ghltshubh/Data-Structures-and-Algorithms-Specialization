import math

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
        for _ in range(n-1):
            previous, current = current, (previous+current) % m
        return current
    
def fibonacci_sum(n):
    m = 10
    _sum = 2 * fibonacci_huge_naive(n, m) + fibonacci_huge_naive(n-1, m) - 1   # sum = fib(n+2) - 1 = 2*fib(n) + fib(n-1) - 1
    return _sum % m


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
