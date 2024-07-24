
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 最长上升子序列(一) 中等
# 给定一个长度为 n 的数组 arr，求它的最长严格上升子序列的长度。
# 所谓子序列，指一个数组删掉一些数（也可以不删）之后，形成的新数组。例如 [1,5,3,7,3] 数组，其子序列有：[1,3,3]、[7] 等。但 [1,6]、[1,3,5] 则不是它的子序列。
# 我们定义一个序列是 严格上升 的，当且仅当该序列不存在两个下标 i 和 j 满足 i < j 且 arr_i >= arr_j
# 数据范围：0 <= n <= 1000
# 要求：空间复杂度O(n), 时间复杂度O(n^2)
# 示例1: 输入：[6,3,1,5,2,3,7], 返回值：4, 说明：该数组最长上升子序列为 [1,2,3,7] ，长度为4


def demo():
    arr = []

if __name__ == '__main__':
    demo()