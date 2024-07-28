
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 判断一个链表是否为回文结构 简单
# 给定一个链表，请判断该链表是否为回文结构。
# 回文是指该字符串正序逆序完全一致。
# 数据范围：链表节点数 0 <= n <= 10^5, 链表中每个节点的值满足 |val| <= 10^7
# 示例1: 输入：{1}, 返回值：true
# 示例2: 输入：{2,1}, 返回值：false, 说明：2->1
# 示例3: 输入：{1,2,2,1}, 返回值：true, 说明：1->2->2->1

# 方法一：复制链表并反转，遍历两个链表 如果元素完全相同则为回文结构
# 方法二：找到链表中间节点，反转前半部分链表或者后半部分链表，遍历两个链表，如果元素完全相同则为回文结构
# 1 -> 2 2 <- 1
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

def reverse(head):
    # [1, 2, 3]
    pre = None
    curr = head
    while curr:
        next = curr.next
        curr.next = pre
        pre = curr
        curr = next
    return pre

def isPail(head):
    # [1,2,2,1], [1,2,3,2,1]
    result = True
    slow = head
    fast = head
    temp = head
    while fast and fast.next:
        fast = fast.next.next
        temp = slow
        slow = slow.next
    mid = slow
    temp.next = None
    righthead = reverse(mid)
    while head and righthead:
        if head.value != righthead.value:
            result = False
            break
        head = head.next
        righthead = righthead.next
    return result

def demo():
    arr = [1]
    arr = [2, 1]
    arr = [1, 2, 2, 1]
    head = list2linkedlist(arr)
    result = isPail(head)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()