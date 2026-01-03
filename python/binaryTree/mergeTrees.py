
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 合并二叉树 简单
# 已知两颗二叉树，将它们合并成一颗二叉树。合并规则是：都存在的结点，就将结点值加起来，否则空的位置就由另一个树的结点来代替。例如：
# 两颗二叉树是: [1, 3, 2, 5]; [2, 1, 3, #, 4, #, 7], 合并后的树为 [3, 4, 5, 5, 4, #, 7]
# 数据范围：树上节点数量满足 0 <= n <= 500, 树上节点的值一定在32位整型范围内。
# 进阶：空间复杂度O(1), 时间复杂度O(n)
# 示例1: 输入：{1,3,2,5},{2,1,3,#,4,#,7}, 返回值：{3,4,5,5,4,#,7}, 说明：如题面图
# 示例2: 输入：{1},{}, 返回值：{1}

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
    while len(curr) > 0:
        temp = []
        for item in curr:
            if item:
                arr.append(item.value)
                temp.append(item.left)
                temp.append(item.right)
            else:
                arr.append('#')
        curr = temp
    while (len(arr) > 0) and (arr[-1] == '#'):
        arr.pop()
    return arr

def mergeTrees(head1, head2):
    curr1 = [head1]
    curr2 = [head2]
    result = []
    while curr1 or curr2:
        num1 = len(curr1)
        num2 = len(curr2)
        num = max(num1, num2)
        temp1 = []
        temp2 = []
        for index in range(num):
            if curr1[index] and curr2[index]:
                value = curr1[index].value + curr2[index].value
                temp1.append(curr1[index].left)
                temp1.append(curr1[index].right)
                temp2.append(curr2[index].left)
                temp2.append(curr2[index].right)
            elif curr1[index]:
                value = curr1[index].value
                temp1.append(curr1[index].left)
                temp1.append(curr1[index].right)
                temp2.append(None)
                temp2.append(None)
            elif curr2[index]:
                value = curr2[index].value
                temp1.append(None)
                temp1.append(None)
                temp2.append(curr2[index].left)
                temp2.append(curr2[index].right)
            else:
                value = '#'
            result.append(value)
        curr1 = temp1
        curr2 = temp2
    new_head = list2tree(result)
    return new_head

def mergeTree_recursive(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    head = TreeNode(head1.value + head2.value)
    head.left = mergeTree_recursive(head1.left, head2.left)
    head.right = mergeTree_recursive(head1.right, head2.right)
    return head

def demo():
    arr1 = [1, 3, 2, 5]
    arr2 = [2, 1, 3, '#', 4, '#', 7]
    # arr1 = [1]
    # arr2 = []
    head1 = list2tree(arr1)
    head2 = list2tree(arr2)
    # new_head = mergeTrees(head1, head2)
    new_head = mergeTree_recursive(head1, head2)
    result = tree2list(new_head)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()