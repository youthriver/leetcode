
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 岛屿数量  中等
# 给一个01矩阵, 1代表是陆地, 0代表海洋, 如果两个1相邻, 那么这两个1属于同一个岛, 我们只考虑上下左右为相邻.
# 岛屿: 相邻陆地可以组成一个岛屿(相邻: 上下左右)判断岛屿个数.
# 例如: 输入 [[1,1,0,0,0],[0,1,0,1,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,1,1,1]]对应的输出为3
# 注: 存储的01数据其实是字符'0','1'
# 备注: 01矩阵范围<=200*200
# 示例一: 输入[[1,1,0,0,0],[0,1,0,1,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,1,1,1]], 返回值为3
# 示例二: 输入[[0]], 返回值为0
# 示例三: 输入[[1,1],[1,1]], 返回值为1

# https://blog.csdn.net/vcj1009784814/article/details/124714547
# 方法一: 深度优先搜索
# 方法二: 广度优先搜索
# 深度优先使用递归，一个方向走到底，广度优先使用一个辅助队列，先处理一个点的所有直接相邻节点
# 方法三: 并查集, 并查集是一种数据结构, 包括合并和查找两种操作,
# 并查集是一种在计算机科学中用于处理一些不交集（Disjoint Sets）的合并及查询问题的数据结构。
# 并查集的主要操作有：
# 1. `Find`: 确定元素属于哪一个子集。它可以被用来确定两个元素是否属于同一子集。
# 2. `Union`: 将两个子集合并成同一个集合。
# 并查集的实现通常可以通过一个整数数组。每个数组的索引代表单个元素，对应的值表示其父节点。根节点的父节点就是它自己。
# 用这种方式实现的并查集，其时间复杂度接近于常数，可以非常高效地处理合并和查找操作。
# 首先将输入的数组中的每个陆地看作一个独立的岛屿, 遍历每一个陆地, 对该元素相邻位置元素(上下左右或者下右)进行搜索, 如果为岛屿则进行合并, 同时岛数目减一
# 最后对并查集中集合数目进行统计, 即为所求结果
# 这种方法的时间复杂度通常为O(n)，其中n为岛屿的数量，因为并查集的合并和查找操作的平均时间复杂度都可以看作是常数时间。

class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        # 根节点p[x] = x
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        self.p[px] = py

def num_of_islands_dsu(arr):
    if not arr:
        return 0
    row = len(arr)
    col = len(arr[0])
    # 先进行岛屿合并
    dsu = DSU(row * col)
    for r in range(row):
        for c in range(col):
            if arr[r][c] == 1:
                positions = [(0, 1), (1, 0)]
                for dr, dc in positions:
                    nr = r + dr
                    nc = c + dc
                    if nr > 0 and nr < row and nc >0 and nc < col and arr[nr][nc] == 1:
                        dsu.union(r*col+c, nr*col+nc)
    # 找到二维数组每个位置的根节点, 构成列表, 去重之后即为独立岛屿数目
    roots = []
    for r in range(row):
        for c in range(col):
            if arr[r][c] == 1:
                index = dsu.find(r*col+c)
                roots.append(index)
    result = len(set(roots))
    return result

def demo():
    arr = [[1,1,0,0,0],[0,1,0,1,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,1,1,1]]
    arr = [[1,1],[1,1]]
    result = num_of_islands_dsu(arr)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()