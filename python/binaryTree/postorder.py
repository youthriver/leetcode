
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s:[%(lineno)d] - %(level)s: %(message)s', level=logging.DEBUG)

# 二叉树的后序遍历  简单
# 给定一个二叉树, 返回他的后序遍历的序列.
# 后序遍历是值按照 左节点 -> 右节点 -> 根节点的顺序的遍历.
# 数据范围: 二叉树的节点数量满足 1<=val<=100, 树的各节点的值各不相同
# 示例一: 输入{1,#,2,3}, 返回值[3,2,1]
# 示例二: 输入{1}, 返回值[1]

class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def demo():
    arr = []

if __name__ == '__main__':
    demo()