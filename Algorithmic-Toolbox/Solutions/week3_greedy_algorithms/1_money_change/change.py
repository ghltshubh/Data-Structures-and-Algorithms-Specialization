import math
def change(money):
    # write your code here
    
    return math.floor(money/10) + math.floor((money % 10)/5) + math.floor(money % 5)


if __name__ == '__main__':
    m = int(input())
    print(change(m))
