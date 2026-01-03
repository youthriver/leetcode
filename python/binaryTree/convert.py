
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 二叉搜索树与双向链表 中等
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。如下图所示
# 二叉搜索树：10 -> 6 -> 4, 6 -> 8, 10 -> 14 -> 12, 14 -> 16, 转变成排序的双向链表：4 ->/<- 6 ->/<- 8 ->/<- 10 ->/<- 12 ->/<- 14 ->/<- 16
# 数据范围：输入二叉树的节点数 0 <= n <= 1000, 二叉树中每个节点的值 0 <= val <= 1000,
# 要求：空间复杂度O(1)(即在原树上操作), 时间复杂度O(n)
# 注意:
# 1.要求不能创建任何新的结点，只能调整树中结点指针的指向。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继
# 2.返回链表中的第一个节点的指针
# 3.函数返回的TreeNode，有左右指针，其实可以看成一个双向链表的数据结构
# 4.你不用输出双向链表，程序会根据你的返回值自动打印输出
# 输入描述：二叉树的根节点
# 返回值描述：双向链表的其中一个头节点。
# 示例1: 输入：{10,6,14,4,8,12,16}, 返回值：From left to right are:4,6,8,10,12,14,16;From right to left are:16,14,12,10,8,6,4; 说明：
# 输入题面图中二叉树，输出的时候将双向链表的头节点返回即可。
# 示例2: 输入：{5,4,#,3,#,2,#,1}, 返回值：From left to right are:1,2,3,4,5;
# From right to left are:5,4,3,2,1;

# 二叉搜索树: 若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
# 若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；任意节点的左、右子树也分别为二叉查找树；
# 二叉查找树相比于其他数据结构的优势在于查找、插入的时间复杂度较低, 为 O(logn)
# 方法一: 递归调用, 将当前处理的子树调整为双向链表，并返回左右两个节点


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def list2tree(arr):
    if len(arr) < 0:
        return None
    head = TreeNode(arr[0])
    curr = [head]
    index = 1
    num = len(arr)
    while (len(curr) > 0) and (index < num):
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
    result = []
    curr = [head]
    while len(curr) > 0:
        temp = []
        for index, item in enumerate(curr):
            if item:
                result.append(item.value)
                if item.left or item.right:
                    temp.append(item.left)
                    temp.append(item.right)
            else:
                if (index != len(curr) - 1) or (len(temp) > 0):
                    result.append('#')
        curr = temp

    return result


def linklist2list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.value)
        curr = curr.right
    return result

def convert(head):
    def recursive(head):
        # 对于当前节点下的二叉树转换为双向链表，并返回左右两侧节点
        if (not head.left) and (not head.right):
            return (head, head)
        if (not head.left):
            left, right = recursive(head.right)
            head.right = left
            left.left = head
            return (head, right)
        if (not head.right):
            left, right = recursive(head.left)
            head.left = right
            right.right = head
            return (left, head)
        left1, right1 = recursive(head.left)
        left2, right2 = recursive(head.right)
        head.left = right1
        right1.right = head
        head.right = left2
        left2.left = head
        return (left1, right2)
    if not head:
        return head
    curr = head
    left, right = recursive(curr)
    return left



def demo():
    arr = [10, 6, 14, 4, 8, 12, 16]
    arr = [5, 4, '#', 3, '#', 2, '#', 1]
    head = list2tree(arr)
    logging.info(f'head is {head.value}')
    head_new = convert(head)
    logging.info(f'head_new is {head_new.value}')
    # result = tree2list(head)
    result = linklist2list(head_new)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()


