
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 矩阵的最小路径和 中等
# 给定一个 n * m 的矩阵 a，从左上角开始每次只能向右或者向下走，最后到达右下角的位置，路径上所有的数字累加起来就是路径和，输出所有的路径中最小的路径和。
# 数据范围：1 <= n, m <= 500, 矩阵中任意值都满足 0 <= a_<i,j> <= 100
# 要求：时间复杂度O(nm)
# 例如：当输入[[1,3,5,9],[8,1,3,4],[5,0,6,1],[8,8,4,0]]时，对应的返回值为12，
# 所选择的最小累加和路径如下图所示：1 -> 3 -> 1 -> 0 -> 6 -> 1 -> 0
# 备注：1 <= n,m <= 2000, 1 <= a_<i,j> <= 100
# 示例1: 输入：[[1,3,5,9],[8,1,3,4],[5,0,6,1],[8,8,4,0]], 返回值：12
# 示例2: 输入：[[1,2,3],[1,2,3]], 返回值：7

def demo():
    arr = []

if __name__ == '__main__':
    demo()