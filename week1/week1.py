# Author:chengjiru
# 2023年09月23日19时40分12秒
# Connect:jiru_cheng@163.com
# 求逆序数对
# A. 逆序对计数单点时限: 2.0 sec，内存限制: 512 MB，计算给出的序列中存在多少逆序对，即有序对
# (i, j) 使得 i < j 但是 a[i] > a[j]。
# acm格式求逆序数对
# 1.归并排序
def merge_sort(nums):
    if len(nums) <= 1:
        return 0
    mid = len(nums) // 2
    # 递归分解
    left = nums[:mid]
    right = nums[mid:]
    ans=merge_sort(left) + merge_sort(right)
    # 合并
    i, j, k = 0, 0, 0 # i,j分别指向左右两个数组的第一个元素，k指向合并后数组的第一个元素
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:#如果左边的数小于等于右边的数，那么就不构成逆序对
            nums[k] = left[i]
            i = i + 1
            k = k + 1
        else:#如果左边的数大于右边的数，那么就构成逆序对
            nums[k] = right[j]
            j = j + 1
            k = k + 1
            ans+=len(left)-i
    while i < len(left):#如果左边的数还有剩余，那么就将左边的数放入临时数组
        nums[k] = left[i]
        i = i + 1
        k = k + 1
    while j < len(right):#如果右边的数还有剩余，那么就将右边的数放入临时数组
        nums[k] = right[j]
        j = j + 1
        k = k + 1
    return ans
if __name__ == '__main__':
    n = eval(input())
    s = list(map(int, input().split()))  # 将输入的字符串转换成列表,map函数的作用是将列表中的每个元素都转换成int类型
    print(merge_sort(s))  # 调用归并排序函数









def merge_sort(s, l, r):
    if l >= r:
        return 0
    mid = (l + r) >> 1  # 取中间值
    res = merge_sort(s, l, mid) + merge_sort(s, mid + 1, r)  # 递归
    i, j = l, mid + 1  # i指的是左边数组的下标，j指的是右边数组的下标
    tmp = []
    while i <= mid and j <= r:
        if s[i] <= s[j]:  # 如果左边的数小于等于右边的数，那么就不构成逆序对
            tmp.append(s[i])
            i += 1
        else:  # 如果左边的数大于右边的数，那么就构成逆序对
            tmp.append(s[j])  # 将右边的数放入临时数组
            j += 1  # 右边的下标加一
            res += mid - i + 1  # 左边的数大于右边的数，那么左边的数后面的数都大于右边的数，所以加上mid-i+1
            pass
        pass
    while i <= mid:  # 如果左边的数还有剩余，那么就将左边的数放入临时数组
        tmp.append(s[i])  # 将左边的数放入临时数组
        i += 1  # 左边的下标加一
        pass
    while j <= r:  # 如果右边的数还有剩余，那么就将右边的数放入临时数组
        tmp.append(s[j])  # 将右边的数放入临时数组
        j += 1  # 右边的下标加一
        pass
    s[l:r + 1] = tmp  # 将临时数组的值赋给s
    return res

if __name__ == '__main__':

    n = eval(input())
    s = list(map(int, input().split()))  # 将输入的字符串转换成列表,map函数的作用是将列表中的每个元素都转换成int类型
    print(merge_sort(s, 0, n - 1))  # 调用归并排序函数


def count_inversions(arr):
    # 帮助函数，用于合并两个子序列并计算逆序对的数量
    def merge(left, right):
        i, j = 0, 0
        count, merged = 0, []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                # 因为left[i:]中的所有元素都大于right[j]
                count += len(left) - i
                # 把剩下的元素加入到merged数组中
        merged.extend(left[i:])
        merged.extend(right[j:])
        return count, merged

        # 递归函数，用于对子序列进行排序并计算逆序对的数量

    def sort(arr):
        if len(arr) <= 1:
            return 0, arr
            # 分割序列为两个子序列
        mid = len(arr) // 2
        inversions, left = sort(arr[:mid])
        inversions_right, right = sort(arr[mid:])
        # 合并子序列并计算逆序对的数量
        inversions_merge, merged = merge(left, right)
        return inversions + inversions_right + inversions_merge, merged

        # 对整个序列进行排序并计算逆序对的数量

    inversions, sorted_arr = sort(arr)
    return inversions


# 从标准输入读取序列的长度和元素
n = int(input())
arr = list(map(int, input().split()))

# 计算逆序对的数量并输出结果
print(count_inversions(arr))

# 数轴上有n个点，每个点有一个坐标 ai。现在需要用数个宽度为k的框体覆盖数轴上全部n个点，求出最少需要的框体数量


