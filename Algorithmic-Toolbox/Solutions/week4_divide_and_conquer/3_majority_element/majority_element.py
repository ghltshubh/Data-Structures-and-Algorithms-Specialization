def majority_element_naive(elements):

    count_dict = {}
    for e in elements:
        count_dict[e] = count_dict.get(e, 0) + 1
        if count_dict[e] > len(elements) / 2:
            return 1
            
    return 0



if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
