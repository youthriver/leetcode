
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 链表中倒数最后k个结点 简单
# 输入一个长度为 n 的链表，设链表中的元素的值为 a_i ，返回该链表中倒数第k个节点。
# 如果该链表长度小于k，请返回一个长度为 0 的链表。
# 数据范围：0 <= n <= 10^5, 0 <= a_i <= 10^9, 0 <= k <= 10^9
# 要求：空间复杂度O(n), 时间复杂度O(n)
# 进阶：空间复杂度O(1), 时间复杂度O(n)
# 例如输入{1,2,3,4,5},2时，对应的链表结构如下图所示：1 -> 2 -> 3 -> 4 -> 5,
# 其中蓝色部分为该链表的最后2个结点，所以返回倒数第2个结点（也即结点值为4的结点）即可，系统会打印后面所有的节点来比较。
# 示例1: 输入：{1,2,3,4,5},2, 返回值：{4,5}, 说明：
# 返回倒数第2个节点4，系统会打印后面所有的节点来比较。
# 示例2: 输入：{2},8, 返回值：{}

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def list2linkedlist(arr):
    head = LinkedList(-1)
    curr = head
    for index, item in enumerate(arr):
        curr.next = LinkedList(item)
        curr = curr.next
    return head.next

def linkedlist2list(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result
def findKthToTail(head, k):
    slow = head
    fast = head
    node = fast
    for index in range(k):
        if not fast:
            return fast
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    return slow

def demo():
    arr = [1, 2, 3, 4, 5]
    k = 2
    arr = [2]
    k = 8
    head = list2linkedlist(arr)
    node = findKthToTail(head, k)
    result = linkedlist2list(node)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()