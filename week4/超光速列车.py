import sys


def min_additional_days(n, k, r, operate_days):
    arr = [0] * (n + 1)
    for i in range(k):
        arr[operate_days[i]] = 1
    add_train = 0  # 需要增加的列车数
    cur = 0  # 当前列车数
    for i in range(1,n+1):
        cur += arr[i]
        if i >= r:
            cur -= arr[i - r]
            while cur < 2:
                j = i
                while (arr[j]):
                    j -= 1
                arr[j] = 1
                cur += 1
                add_train += 1
    return add_train


if __name__ == '__main__':
    n, k, r = map(int, input().split())
    operate_days = []
    for i in range(k):
        number = int(sys.stdin.readline().strip())
        operate_days.append(number)
    result = min_additional_days(n, k, r, operate_days)
    print(result)





