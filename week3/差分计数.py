# Author:chengjiru
# 2023年10月16日20时48分34秒
# Connect:jiru_cheng@163.com
#有一组 1 维的物品需要打包进一批同样的箱子中。所有的箱子有完全一样的长度 l 以及每一个物品长度 li<=l. 我们要找到一个最小的数字 q, 使得 : 1. q 个箱子足以装下全部的物品。 2. 对于任意一个物品而言, 无论它的长度是多少, 都可以在这 q 个箱子中的某些个装下它。 3. 所有的物品都不会被浪费。 请问, 这个最小的数字 q 是多少?
# 输入:第一行两个整数 n 和 l, 表示物品的数量以及箱子的长度。第二行 n 个整数, 表示每一个物品的长度。
# 输出:输出一个整数 q, 表示答案。
def min_boxes(n, l, items):
    items.sort()  # 按长度从小到大排序
    left = 0
    right = n - 1
    boxes = 0

    while left <= right:
        current_box_capacity = 0
        items_in_box = 0

        # 尝试将两个物品放入当前箱子
        while left <= right and items_in_box < 2 and current_box_capacity + items[right] <= l:
            current_box_capacity += items[right]
            right -= 1
            items_in_box += 1

        while left <= right and items_in_box < 2 and current_box_capacity + items[left] <= l:
            current_box_capacity += items[left]
            left += 1
            items_in_box += 1

        # 放满一个箱子，箱子数量加一
        boxes += 1

    return boxes

# 读取输入
n = int(input())
l = int(input())
items = [int(input()) for _ in range(n)]

# 计算最小箱子总数
result = min_boxes(n, l, items)

# 输出结果
print(result)


