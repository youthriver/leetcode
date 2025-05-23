
import logging
import os

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 在一个二维数组array中(每个一维数组的长度相同), 每一行都按照从左到右递增的顺序排列, 每一列都按照从上到下递增的顺序排序.
# 请完成一个函数, 输入这样的一个二维数组和一个整数, 判断数组中是否含有该整数.
# [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], 给定target=7, 返回true, 给定target=3, 返回false.
# 数据范围: 矩阵的长宽满足0<=n, m <= 500, 矩阵中的值满足0<=val<=10^9
# 进阶: 空间复杂度O(1), 时间复杂度O(n+m)
# 示例1: 输入7, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], 返回值true, 说明: 存在7, 返回true
# 示例2: 输入1, [[2]], 返回值false
# 示例3: 输入3, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], 返回值false, 说明: 不存在3, 返回false

# 将target与右上角或左下角元素进行比较, 这样每次能去除一列或者一行

def findNumberIn2DArray(arr, target):
    row = len(arr)
    col = len(arr[0])
    for m in range(row):
        if target < arr[m][0]:
            return False
        if target > arr[m][-1]:
            continue
        for n in range(col):
            if target == arr[m][n]:
                logging.info(f'row is {m}, col is {n}')
                return True
    return False

def demo():
    arr = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    target = 7
    # arr = [[2]]
    # target = 1
    # arr = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    # target = 3
    result = findNumberIn2DArray(arr, target)
    logging.info(result)


if __name__ == '__main__':
    demo()