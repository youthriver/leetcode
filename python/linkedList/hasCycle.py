
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 判断链表中是否有环 简单
# 判断给定的链表中是否有环。如果有环则返回true，否则返回false。
# 数据范围：链表长度 0 <= n <= 10000, 链表中任意节点的值满足 |val| <= 100000
# 要求：空间复杂度O(1), 时间复杂度O(n)
# 输入分为两部分，第一部分为链表，第二部分代表是否有环，然后将组成的head头结点传入到函数里面。-1代表无环，其它的数字代表有环，这些参数解释仅仅是为了方便读者自测调试。实际在编程时读入的是链表的头节点。
# 例如输入{3,2,0,-4},1时，对应的链表结构如下图所示： 3 -> 2 -> 0 -> -4 -> 2
# 可以看出环的入口结点为从头结点开始的第1个结点（注：头结点为第0个结点），所以输出true。
# 示例1: 输入：{3,2,0,-4},1, 返回值：true, 说明：
# 第一部分{3,2,0,-4}代表一个链表，第二部分的1表示，-4到位置1（注：头结点为位置0），即-4->2存在一个链接，组成传入的head为一个带环的链表，返回true
# 示例2: 输入：{1},-1, 返回值：false, 说明：
# 第一部分{1}代表一个链表，-1代表无环，组成传入head为一个无环的单链表，返回false
# 示例3: 输入：{-1,-7,7,-4,19,6,-9,-5,-2,-5},6, 返回值：true

# 方法一：遍历链表，遇到node为空或者出现过则终止，为空则返回false, 出现过返回True

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def list2linkedlist(arr, node):
    head = LinkedList(-1)
    curr = head
    for index, item in enumerate(arr):
        curr.next = LinkedList(item)
        curr = curr.next
    next = head
    index = -1
    if node > -1:
        while next:
            if index == node:
                curr.next = next
                break
            next = next.next
            index += 1

    return head.next

def hasCycle(head):
    result = False
    temp = {}
    while head:
        if head not in temp:
            temp[head] = 1
            head = head.next
        else:
            result = True
            break
    return result

def demo():
    arr = [3, 2, 0, -4]
    node = 1
    # arr = [1]
    # node = -1
    arr = [-1, -7, 7, -4, 19, 6, -9, -5, -2, -5]
    node = 6
    head = list2linkedlist(arr, node)
    result = hasCycle(head)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()