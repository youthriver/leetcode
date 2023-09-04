
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 将一个节点数为size链表m位置到n位置之间的区间反转, 要求时间复杂度为o(n), 空间复杂度为o(1)
# 例如: 给出的链表为 1 -> 2 -> 3 -> 4 -> 5 -> NULL, m=2, n=4, 返回 1 -> 4 -> 3 -> 2 -> 5 -> NULL
# 数据范围: 链表长度 0 < size <= 1000, 0 < m <= n <= size, 链表中每个节点的值满足 |val| <= 1000
# 要求: 时间复杂度o(n), 空间复杂度o(n)
# 进阶: 时间复杂度o(n), 空间复杂度o(1)
# 示例1: 输入 {1, 2, 3, 4, 5}, 2, 4, 返回值{1, 4, 3, 2, 5}
# 示例2: 输入 {5}, 1, 1, 返回值{5}

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def createLinkedList(arr):
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        node = ListNode(arr[i])
        curr.next = node
        curr = node
    return head

def create2linkedlist():
    head = ListNode(1)
    p1 = ListNode(2)
    p2 = ListNode(3)
    p3 = ListNode(4)
    head.next = p1
    p1.next = p2
    p2.next = p3
    return head

def reverseLinkedList_fromMtoN(linkedlist, m, n):
    if n < m:
        return linkedlist
    index = 0
    curr = linkedlist
    while curr:
        index += 1
        if index == m - 1:
            left = curr
        if index == n:
            right = curr.next
            break
        curr = curr.next
    start = left.next
    end = curr
    left.next = None
    end.next = None
    curr = start
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    start.next = right
    left.next = prev

    return linkedlist

def demo():
    arr = [1, 2, 3, 4, 5]
    m = 2
    n = 4
    linkedlist = createLinkedList(arr)
    result = reverseLinkedList_fromMtoN(linkedlist, m, n)
    logging.info(f'result is {result}')
    while result:
        logging.info(result.val)
        result = result.next

if __name__ == '__main__':
    demo()