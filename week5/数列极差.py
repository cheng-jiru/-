import sys
def max_arr(numbers_list:list):
    numbers = numbers_list.copy()
    numbers.sort()
    while len(numbers)>1:
        a = numbers.pop(0)
        b = numbers.pop(0)
        new_num = a * b + 1
        numbers.append(new_num)
        numbers.sort()
    return numbers[0]

def min_arr(numbers_list:list):
    numbers = numbers_list.copy()
    numbers.sort(reverse=True)
    while len(numbers)>1:
        a = numbers.pop(0)
        b = numbers.pop(0)
        new_num = a * b + 1
        numbers.append(new_num)
        numbers.sort(reverse=True)
    return numbers[0]



if __name__ == '__main__':
    n=int(input())
    numbers=[]
    for i in range(n):
        number = int(sys.stdin.readline().strip())
        numbers.append(number)
    max=max_arr(numbers)
    min=min_arr(numbers)
    print(max-min)