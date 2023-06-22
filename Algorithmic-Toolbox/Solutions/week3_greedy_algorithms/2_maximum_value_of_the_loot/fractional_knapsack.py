from sys import stdin
import numpy as np

def optimal_value(capacity, weights, values):
    value = 0.
    i = 0
    # write your code here
    for _ in range(n):
        if capacity == 0:
            return value
        
        value_per_weight = np.array(values)/np.array(weights)
        value_per_weight[value_per_weight == np.inf] = 0
        i = np.argmax(value_per_weight)
        a = min(weights[i], capacity)
        value = value + a * values[i] / weights[i]
        weights[i] = weights[i] - a
        capacity = capacity - a

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    # print(n, capacity, values, weights)
    opt_value = optimal_value(capacity, weights, values)   
    print("{:.10f}".format(opt_value))
