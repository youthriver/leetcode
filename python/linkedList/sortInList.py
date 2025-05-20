
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 单链表的排序 中等
# 给定一个节点数为n的无序单链表，对其按升序排序。
# 数据范围：0 < n < 100000, 保证节点权值在 [-10^9, 10^9]之内
# 要求：空间复杂度O(n), 时间复杂度O(nlogn)
# 示例1: 输入：[1,3,2,4,5], 返回值：{1,2,3,4,5}
# 示例2: 输入：[-1,0,-2], 返回值：{-2,-1,0}

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
def list2linkedlist(arr):
    head = LinkedList(-1)
    curr = head
    for item in arr:
        curr.next = LinkedList(item)
        curr = curr.next
    return head.next

def linkedlist2list(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result

def get_mid(head):
    slow = head
    fast = head
    while fast and fast.next:
        temp = slow
        slow = slow.next
        fast = fast.next.next
    return temp
def sortInList(head):
    if (not head) or (not head.next):
        return head
    mid = get_mid(head)
    right = mid.next
    left = mid
    left.next = None
    left_linkedlist = sortInList(head)
    right_linkedlist = sortInList(right)
    result = merge(left_linkedlist, right_linkedlist)
    return result

def merge(left, right):
    head = LinkedList(-1)
    curr = head
    while left and right:
        if (left.value <= right.value):
            curr.next = left
            curr = curr.next
            left = left.next
        else:
            curr.next = right
            curr = curr.next
            right = right.next
    while left:
        curr.next = left
        curr = curr.next
        left = left.next
    while right:
        curr.next = right
        curr = curr.next
        right = right.next
    return head.next

def demo():
    arr = [1, 3, 2, 4, 5]
    arr = [-1, 0, 2]
    head = list2linkedlist(arr)
    node = sortInList(head)
    result = linkedlist2list(node)
    logging.info(f'result is {result}')


if __name__ == '__main__':
    demo()