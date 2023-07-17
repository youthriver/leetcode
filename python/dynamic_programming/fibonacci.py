
import logging
import os

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 输入一个正整数n, 输出斐波那契数列的第n项
# f(n) = f(n-1) + f(n-2), f(1)=f(2)=1
# 1 <= n <= 40
# 空间复杂度o(1), 时间复杂度o(n), 也有时间复杂度o(logn)的解法
# 4 -> 3
# 1 -> 1
# 2 -> 1

def fibonacci(num):
    if num < 3:
        return 1
    f_1 = 1
    f_2 = 1
    for i in range(3, num + 1):
        f_n = f_1 + f_2
        f_1 = f_2
        f_2 = f_n

    return f_n

def demo():
    num = 4
    result = fibonacci(num)
    logging.info(result)


if __name__ == '__main__':
    demo()