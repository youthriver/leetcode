
import logging
import os

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 一个数组A中存有n个整数, 在不允许使用另外数组的前提下, 将每个整数循环向右移M(M>=0)个位置, 即将A中的数据由(A_0A_1 ... A_(N-1))变换为
# (A_(N-M) ... A_(N-1)A_0A_1 ... A(N-M-1)), (最后M个数循环移至最前面的M个位置). 如果需要考虑移动数据的次数尽量少, 要如何设计移动的方法?
# 数据范围: 0 < n <= 100, 0 <= m <= 1000
# 进阶: 空间复杂度o(1), 时间复杂度o(n)
# 1 <= N <= 100, M >= 0
# 6, 2, [1,2,3,4,5,6] -> [5,6,1,2,3,4]
# 4, 0, [1,2,3,4] -> [1,2,3,4]

def rotate(arr):
    return

def demo():
    arr = []
    result = rotate(arr)
    logging.info(result)

if __name__ == '__main__':
    demo()