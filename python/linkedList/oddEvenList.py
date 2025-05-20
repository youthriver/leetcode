
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 链表的奇偶重排 中等
# 给定一个单链表，请设定一个函数，将链表的奇数位节点和偶数位节点分别放在一起，重排后输出。
# 注意是节点的编号而非节点的数值。
# 数据范围：节点数量满足 0 <= n <= 10^5, 节点中的值都满足 0 <= val <= 1000
# 要求：空间复杂度O(n), 时间复杂度O(n)
# 示例1: 输入：{1,2,3,4,5,6}, 返回值：{1,3,5,2,4,6}, 说明：1->2->3->4->5->6->NULL, 重排后为 1->3->5->2->4->6->NULL
# 示例2: 输入：{1,4,6,3,7}, 返回值：{1,6,7,4,3}, 说明：1->4->6->3->7->NULL, 重排后为 1->6->7->4->3->NULL
# 奇数位节点有1,6,7，偶数位节点有4,3。重排后为1,6,7,4,3
# 备注：链表长度不大于200000。每个数范围均在int内。

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

def oddEvenList(head):
    if (not head) or (not head.next):
        return head
    odd = head
    even = head.next
    temp = even
    while even.next and even.next.next:
        odd.next = even.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
    if even.next:
        odd.next = even.next
        odd = odd.next
        even.next = None
    odd.next = temp

    return head

def demo():
    arr = [1, 2, 3, 4, 5, 6]
    # arr = [1, 4, 6, 3, 7]
    head = list2linkedlist(arr)
    node = oddEvenList(head)
    result = linkedlist2list(node)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()