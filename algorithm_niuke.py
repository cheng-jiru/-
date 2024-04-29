# 牛客算法 循环队列
# 题目需求：循环队列
"""
描述
请你实现一个循环队列，该循环队列可利用的空间大小等于n个int型变量的大小。
操作：
push x：将x加入到循环队列尾端。若循环队列已满，输出"full"(不含引号)，否则不输出任何内容。保证
x为int型整数。
front：输出队首元素，队首不出队。若队列为空，输出"empty"(不含引号)。
pop：输出队首元素，且队首出队。若队列为空，输出"empty"(不含引号)。
输入描述：
"""


class Queue:
    def __init__(self, n):
        self.n = n
        self.queue = []
        self.front = 0
        self.rear = 0

    def push(self, x: int):
        if self.rear == self.n:
            print("full")
        else:
            self.queue.append(x)
            self.rear += 1


