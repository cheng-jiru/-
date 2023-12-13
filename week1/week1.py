import sys


def Count(x, arr):
    count = 0
    freq_map = {}
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1
    for num in arr:
        # 验证ai+x是否在数组中

        if num + x in freq_map:  # 这里的freq_map主要是搜寻键，即数组中的数
            count += freq_map[num + x]
        if num - x in freq_map:
            count += freq_map[num - x]

    return count // 2


if __name__ == '__main__':
    n, x = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    print(Count(x, arr))