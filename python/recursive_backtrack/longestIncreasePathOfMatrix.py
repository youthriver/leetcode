
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

def demo():
    arr = []

if __name__ == '__main__':
    demo()