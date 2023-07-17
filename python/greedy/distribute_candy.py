
import logging
import os

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 根据游戏得分来发糖果, 要求如下:
# 1. 每个孩子最少分到一个糖果
# 2. 任意两个相邻的孩子, 得分较多的孩子必须拿多一些糖果(若是相同则无此限制)
# 给定一个数组arr代表得分数组, 请返回最少需要多少糖果
# 要求: 时间复杂度o(n), 空间复杂度o(n)
# 数据范围: 1 <= n <= 100000, 1 <= a_i <= 1000
# [1,1,2] -> 4=1+1+2
# [1,1,1] -> 3=1+1+1

def distribute_candy(arr):
    return

def demo():
    arr = []
    result = distribute_candy(arr)
    logging.info(result)

if __name__ == '__main__':
    demo()