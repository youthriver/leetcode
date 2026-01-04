
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 二叉树的镜像 简单
# 操作给定的二叉树，将其变换为源二叉树的镜像。
# 数据范围：二叉树的节点数 0 <= n <= 1000, 二叉树每个节点的值 0 <= val <= 1000
# 要求：空间复杂度O(n), 本题也有原地操作，即空间复杂度O(1)的解法, 时间复杂度O(n)
# 比如：源二叉树 [8, 6, 10, 5, 7, 9, 11], 镜像二叉树 [8, 10, 6, 11, 9, 7, 5]
# 示例1: 输入：{8,6,10,5,7,9,11}, 返回值：{8,10,6,11,9,7,5}, 说明：如题面所示
# 示例2: 输入：{}, 返回值：{}


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def list2tree(arr):
    num = len(arr)
    if num < 1:
        return None
    head = TreeNode(arr[0])
    curr = [head]
    index = 1
    while (index < num):
        temp = []
        for item in curr:
            if (index < num) and (arr[index] != '#'):
                item.left = TreeNode(arr[index])
                temp.append(item.left)
            index += 1
            if (index < num) and (arr[index] != '#'):
                item.right = TreeNode(arr[index])
                temp.append(item.right)
            index += 1
        curr = temp
    return head

def tree2list(head):
    arr = []
    curr = [head]
    while curr:
        temp = []
        for item in curr:
            if item:
                arr.append(item.value)
                temp.append(item.left)
                temp.append(item.right)
            else:
                arr.append('#')
        curr = temp
    while (arr) and (arr[-1] == '#'):
        arr.pop()
    return arr

def mirror(head):
    if not head:
        return None
    if head.left or head.right:
        temp = head.left
        head.left = head.right
        head.right = temp
    if head.left:
        mirror(head.left)
    if head.right:
        mirror(head.right)
    return head

def demo():
    arr = [8, 6, 10, 5, 7, 9, 11]
    # arr = []
    head = list2tree(arr)
    new_head = mirror(head)
    result = tree2list(new_head)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()