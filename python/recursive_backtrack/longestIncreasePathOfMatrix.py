
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 矩阵最长递增路径 中等
# 给定一个 n 行 m 列矩阵 matrix ，矩阵内所有数均为非负整数。 你需要在矩阵中找到一条最长路径，使这条路径上的元素是递增的。并输出这条最长路径的长度。
# 这个路径必须满足以下条件：
# 1. 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外。
# 2. 你不能走重复的单元格。即每个格子最多只能走一次。
# 数据范围：1 <= n, m <= 1000, 0 <= matrix[i][j] <= 1000
# 进阶：空间复杂度 O(nm), 时间复杂度O(nm)
# 例如：当输入为[[1,2,3],[4,5,6],[7,8,9]]时，对应的输出为5，
# 其中的一条最长递增路径如下图所示：1 -> 2 -> 3 -> 6 -> 9
# 示例1: 输入：[[1,2,3],[4,5,6],[7,8,9]], 返回值：5, 说明：1->2->3->6->9即可。当然这种递增路径不是唯一的。
# 示例1: 输入：[[1,2],[4,3]], 返回值：4, 说明：1->2->3->4
# 备注：矩阵的长和宽均不大于1000，矩阵内每个数不大于1000

# 方法一：递归实现，

# 不可变对象（数字、字符、字符串、元祖等）
# 可变对象（列表、字典等）
# id函数（用于求变量地址）
# nonlocal关键字是声明我这里用的是外部的result，而不是自己新定义的局部变量result

def longestIncreasePathOfMatrix(arr):
    def recursive(arr, visited, row, col, cur):
        node = arr[row][col]
        visited[row][col] = True
        # 如果四周全部遍历过或无递增元素，则当前路径截止，将当前长度与result进行比较，如果大于result, 则更新result
        neighbors = [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]
        for neighbor in neighbors:
            cur_row = neighbor[0]
            cur_col = neighbor[1]
            if (cur_row >= 0) and (cur_row < n) and (cur_col >= 0) and (cur_col < m) and (not visited[cur_row][cur_col]) and (arr[cur_row][cur_col] > node):
                recursive(arr, visited, cur_row, cur_col, cur+1)
            else:
                nonlocal result
                if cur > result:
                    result = cur
    result = 0
    n = len(arr)
    m = len(arr[0])
    # 不能写visited = [[False] * m] * n, 这样会使后面n-1行是第1行的引用, 修改visited[0][0] = 0会使第一列所有元素值变为0
    visited = [[False for _ in range(m)] for _ in range(n)]
    # 记录当前长度
    cur = 1
    # 记录当前位置，从(0, 0)开始移动
    row, col = 0, 0
    recursive(arr, visited, row, col, cur)
    return result

def demo():
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    arr = [[1, 2], [4, 3]]
    result = longestIncreasePathOfMatrix(arr)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()