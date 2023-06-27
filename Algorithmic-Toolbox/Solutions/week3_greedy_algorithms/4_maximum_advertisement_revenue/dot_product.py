import numpy as np


def max_dot_product(first_sequence, second_sequence):
    first_sequence = np.array(sorted(first_sequence))
    second_sequence = np.array(sorted(second_sequence))
    max_product = np.dot(first_sequence, second_sequence)
    return max_product


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
