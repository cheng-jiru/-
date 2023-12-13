from bisect import bisect_right as br

fib = [1, 1]
while fib[-1] < 1e18:
    fib.append(fib[-1] + fib[-2])


def split(x):
    while x > 0:
        idx = br(fib, x) - 1
        x -= fib[idx]
        yield idx


def dp(l):
    sp, nsp = (l[0] - 1) // 2, 1
    for cur, pre in zip(l[1:], l):
        sp, nsp = (cur - pre) // 2 * sp + (cur - pre - 1) // 2 * nsp, sp + nsp
    return sp + nsp


for t in range(int(input())):
    print(f'case #{t}:')
    print(dp(list(split(int(input())))[::-1]))