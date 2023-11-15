
import logging
import os

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)


# 给定一个二叉树的根节点root, 返回它的中序遍历结果
# 数据范围: 树上节点数满足0<=n<=1000, 树上每个节点的值满足 -1000 <= val <= 1000
# 进阶: 空间复杂度O(n), 时间复杂度O(n)
# 备注: 树中节点数目在范围[0, 100]内树中的节点的值在[-100, 100]以内
# 示例1: 输入{1, 2, #, #, 3}, 返回值[2, 3, 1]
# 示例2: 输入{}, 返回值[]
# 示例3: 输入{1, 2}, 返回值[2, 1]
# 示例4: 输入{1, #, 2}, 返回值[1, 2]

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def list2tree(arr):
    # 对于index为i的节点, 左右子节点index分别为 2*i+1, 2*i+2
    root = TreeNode(arr[0])
    queues = [root]
    num = len(arr)
    for index, item in enumerate(arr):
        if not item:
            continue
        curr = queues[0]
        if (index * 2 + 1 < num) and arr[index * 2 + 1]:
            curr.left = TreeNode(arr[2 * index + 1])
            queues.append(curr.left)
        if (index * 2 + 2 < num) and arr[index * 2 + 2]:
            curr.right = TreeNode(arr[2 * index + 2])
            queues.append(curr.right)
        del queues[0]
    return root

def list2tree_recursive(arr):
    def trans(index):
        if (index >= len(arr)) or (arr[index] is None):
            return None
        tmp = TreeNode(arr[index])
        tmp.left = trans(index * 2 + 1)
        tmp.right = trans(index * 2 + 2)
        return tmp
    root = trans(0)
    return root

def inorder(root):
    result = []
    stacks = [root.left]
    while stacks:
        temp = stacks[0]
        if temp:
            stacks.append(temp.left)
            result.append(temp.value)
            stacks.append(temp.right)
        del stacks[0]

    return result

def inorder_recursive(root):
    def trans(root):
        if root:

            trans(root.left)
            result.append(root.value)
            trans(root.right)
    result = []
    trans(root)
    return result

def demo():
    arr = [1, 2, None, None, 3]
    # root = list2tree(arr)
    root = list2tree_recursive(arr)
    # result = inorder_recursive(root)
    result = inorder(root)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()