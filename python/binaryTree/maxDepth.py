

import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 二叉树的最大深度 简单
# 求给定二叉树的最大深度，深度是指树的根结点到任一叶子结点路径上节点的数量。最大深度是所有叶子结点的深度的最大值。（注：叶子结点是指没有子节点的节点。）
# 数据范围：0<=n<=100000，树上每个节点的val满足|val|<=100
# 要求：空间复杂度O(1)，时间复杂度O(n)
# 示例一：输入：{1, 2}，返回值：2
# 示例二：输入：{1, 2, 3, 4, #, #, 5}，返回值：3

# 对于根节点为i的元素, 其左节点坐标为2*i+1, 右节点坐标为2*i+2
# 方法一: 递归遍历, 深度优先, 找到最大深度
# 方法二: 迭代法, 广度优先, 层次遍历

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def list2tree(arr):
    result = []
    for item in arr:
        if item != '#':
            result.append(TreeNode(item))
        else:
            result.append(None)
    for index, item in enumerate(arr):
        cur = result[index]
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        if (left_index < len(arr)) and (arr[left_index] != '#'):
            cur.left = result[left_index]
        if (right_index < len(arr)) and (arr[right_index] != '#'):
            cur.right = result[right_index]
    return result[0] if len(result) > 0 else None

def maxDepth(root):
    depth = 0
    def recursive(root, depth):
        if root.left or root.right:
            if root.left:
                depth_left = recursive(root.left, depth + 1)
            else:
                depth_left = depth
            if root.right:
                depth_right = recursive(root.right, depth + 1)
            else:
                depth_right = depth
            return max(depth_left, depth_right)
        else:
            return depth
    if root:
        depth = recursive(root, 1)
    return depth


def demo():
    arr = [1, 2, 3, 4, '#', '#', 5]
    arr = [1, 2]
    arr = []
    root = list2tree(arr)
    depth = maxDepth(root)
    logging.info(f'max depth is {depth}')

if __name__ == '__main__':
    demo()