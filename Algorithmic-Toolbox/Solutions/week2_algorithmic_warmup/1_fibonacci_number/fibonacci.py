def fibonacci_number(n):
    fibList = [0] * (n+1)
    if n <= 1:
        return n
    else:
        fibList[0] = 0
        fibList[1] = 1
        for i in range(2, n+1):
            fibList[i] = fibList[i-1] + fibList[i-2]
        return fibList[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
