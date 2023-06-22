def max_pairwise_product(numbers):
    n = len(numbers)
    
  
    max_num1 = 0
    max_num2 = 0
    for i in range(n):
        if numbers[i] > max_num1:
            max_num2 = max_num1
            max_num1 = numbers[i]
        elif numbers[i] > max_num2:
            max_num2 = numbers[i]

    return max_num2 * max_num1


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
