# Author:chengjiru
# 2023年10月16日19时37分57秒
# Connect:jiru_cheng@163.com
# 输入:第一行一个整数n，表示序列的长度。第二行n个整数，表示序列的每个数。
# 输出:输出最长上升子序列的长度。
def Lis(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp)


if __name__ == '__main__':
    n = eval(input())
    s = list(map(int, input().split()))  # 将输入的字符串转换成列表,map函数的作用是将列表中的每个元素都转换成int类型
    print(Lis(s))  # 调用归并排序函数


# Dynamic programming + Dichotomy.

def lengthOfLIS(nums):
    tails, res = [0] * len(nums), 0 #res表示最长上升子序列的长度
    for num in nums:#tails数组表示长度为i+1的上升子序列的末尾元素的最小值
        i, j = 0, res #i表示左边界，j表示右边界
        while i < j:
            m = (i + j) // 2
            if tails[m] < num:
                i = m + 1  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
            else:
                j = m
        tails[i] = num
        if j == res: res += 1
    return res
