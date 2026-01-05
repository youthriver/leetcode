
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 判断是不是二叉搜索树 中等
# 给定一个二叉树根节点，请你判断这棵树是不是二叉搜索树。
# 二叉搜索树满足每个节点的左子树上的所有节点均小于当前节点且右子树上的所有节点均大于当前节点。
# 例：[1, 2, 3], [2, 1, 3]
# 数据范围：节点数量满足 1 <= n <= 10^4, 节点上的值满足 -2^31 <= val <= 2^31 - 1
# 要求：空间复杂度O(), 时间复杂度O()
# 示例1: 输入：{1,2,3}, 返回值：false, 说明：如题面图1
# 示例2: 输入：{2,1,3}, 返回值：true, 说明：如题面图2

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
    while index < num:
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

def isValidBST(head):
    def recursive(head):
        # 对于左边节点记录最大值，对于右边节点记录最小值
        if (not head.left) and (not head.right):
            return head.value
        if head.left:
            left_min, left_max = recursive(head.left)
        if head.right:
            right_min, right_max = recursive(head.right)

    return result

def demo():
    arr = [1, 2, 3]
    # arr = [2, 1, 3]
    arr = [3,2,5,1,4]   # false
    head = list2tree(arr)
    result = isValidBST(head)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()