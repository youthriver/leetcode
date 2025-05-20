
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s:[%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 二叉树的后序遍历  简单
# 给定一个二叉树, 返回他的后序遍历的序列.
# 后序遍历是值按照 左节点 -> 右节点 -> 根节点的顺序的遍历.
# 数据范围: 二叉树的节点数量满足 1<=val<=100, 树的各节点的值各不相同
# 示例一: 输入{1,#,2,3}, 返回值[3,2,1]
# 示例二: 输入{1}, 返回值[1]

# list2tree方法一: 在列表中index位置节点的左右节点坐标为 2*index+1, 2*index+2,
# 此题输入#节点的后续子节点在列表中均无体现, 对于index节点, 假设前面有n个#, 则其左右子节点位置为 2*index+1-2*n, 2*index+2-2*n
# 依照此方法可以将列表转为二叉树结构

# 后序遍历方法一: 递归方法
# 后序遍历方法二: 非递归方法, 借助一个列表存储按顺序遍历过的节点
# 还是不会, 需要继续看这个题

class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def list2tree(arr):
    num_none = 0
    num = len(arr)
    if num == 0:
        return None
    nodes = [None] * num
    nodes[0] = TreeNode(arr[0])
    for index, item in enumerate(arr):
        if item:
            node = nodes[index]
            left = 2 * index + 1 - 2 * num_none
            right = 2 * index + 2 - 2 * num_none
            if (left < num) and (arr[left]):
                nodes[left] = TreeNode(arr[left])
                node.left = nodes[left]
            if (right < num) and (arr[right]):
                nodes[right] = TreeNode(arr[right])
                node.right = nodes[right]
            # nodes[index] = node
        else:
            num_none += 1

    return nodes[0]

def postorder(root):
    result = []
    stacks = []
    temp = root
    while (temp) or (len(stacks) > 0):
        while temp:
            stacks.append(temp)
            # 能左就左，不能左就右
            if temp.left:
                temp = temp.left
            else:
                temp = temp.right
        # 只有在遍历到根节点进行取值的时候才使用pop操作, 将其从遍历队列中取出
        curr = stacks.pop()
        result.append(curr.value)
        if (len(stacks) > 0) and (curr == stacks[-1].left):
            temp = stacks[-1].right
        else:
            temp = None

    return result

def postorder_recursive(root):
    result = []
    def trans(node):
        if node:
            trans(node.left)
            trans(node.right)
            result.append(node.value)
    trans(root)
    return result


def demo():
    arr = [1, None, 2, 3]
    root = list2tree(arr)
    # result = postorder_recursive(root)
    result = postorder(root)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()