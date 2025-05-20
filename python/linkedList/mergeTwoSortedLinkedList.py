
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 合并两个排序的链表  简单
# 输入两个递增的链表, 单个链表的长度为n, 合并这两个链表并使新链表中的节点仍然是递增排序的.
# 数据范围: 0<=n<=1000, -1000<=节点值<=1000
# 要求: 空间复杂度O(1), 时间复杂度O(n)
# 如输入{1,3,5},{2,4,6},合并后的链表为{1,2,3,4,5,6}, 所以对应的输出为{1,2,3,4,5,6}
# 或输入{-1,2,4},{1,3,4}时, 合并后的链表为{-1,1,2,3,4,4}
# 示例一: 输入[1,3,5],[2,4,6],返回值[1,2,3,4,5,6]
# 示例二: 输入[],[],返回值[]
# 示例三: 输入[-1,2,4],[1,3,4],返回值[-1,1,2,3,4,4]

# 定义一个LinkedList结构变量, 其值是一个地址
# 当前变量对象cur如果取到None值, 再往下赋值链表会断开
# 方法一: 迭代
# 方法二: 递归


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def list2linkedlist(arr):
    root = None
    for index, item in enumerate(arr):
        if index == 0:
            root = LinkedList(item)
            before = root
        else:
            cur = LinkedList(item)
            before.next = cur
            before = cur
    return root


def linkedlist2list(root):
    result = []
    while root:
        result.append(root.value)
        root = root.next
    return result

def merge_two_sorted_linkedlist(root1, root2):
    root = LinkedList(-1)
    cur = root

    index1 = root1
    index2 = root2
    while (index1 and index2):
        if (index1.value <= index2.value):
            value = index1.value
            index1 = index1.next
        else:
            value = index2.value
            index2 = index2.next
        cur.next = LinkedList(value)
        cur = cur.next

    while index1:
        value = index1.value
        index1 = index1.next
        cur.next = LinkedList(value)
        cur  = cur.next
    while index2:
        value = index2.value
        index2 = index2.next
        cur.next = LinkedList(value)
        cur = cur.next

    return root.next

def demo():
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    arr1 = []
    arr2 = []
    arr1 = [-1, 2, 4]
    arr2 = [1, 3, 4]
    root1 = list2linkedlist(arr1)
    root2 = list2linkedlist(arr2)
    root = merge_two_sorted_linkedlist(root1, root2)
    result = linkedlist2list(root)
    logging.info(f'result is {result}')


if __name__ == '__main__':
    demo()