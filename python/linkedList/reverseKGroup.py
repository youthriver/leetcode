
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 链表中的节点每k个一组翻转 - 中等
# 将给出的链表中的节点每k个一组翻转, 返回翻转后的链表
# 如果链表中的节点数不是k的倍数, 将最后剩下的节点保持原样
# 你不能更改节点中的值, 只能更改节点本身
# 数据范围: 0<=n<=2000, 1<=k<=2000, 链表中每个元素都满足0<=val<=1000
# 要求空间复杂度O(1), 时间复杂度O(n)
# 例如: 给定的链表是 1->2->3->4->5
# 对于k=2, 你应该返回2->1->4->3->5
# 对于k=3, 你应该返回3->2->1->4->5
# 示例一: 输入{1,2,3,4,5},2, 返回值{2,1,4,3,5}
# 示例二: 输入{},1, 返回值{}

# 方法一: 增加一个空节点作为链表头, 翻转完成后, 空节点的next即为新的翻转后的链表头; 以k个为一组, 进行翻转, 记录k个一组之前和之后的节点, 翻转完成后把翻转结果放回原链表

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def list2linkedlist(arr):
    if len(arr) == 0:
        return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        node = ListNode(arr[i])
        curr.next = node
        curr = node
    return head

def linkedlist2list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

def reverse(start, end):
    curr = start
    prev = None
    while curr != end:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    end.next = prev
    return end, start

def reverseKGroup(head, k):
    new_head = ListNode(-1)
    new_head.next = head
    pre = new_head
    curr = head
    start = curr
    index = 0
    while curr:
        index += 1
        if index % k == 0:
            end = curr
            after = end.next
            start, end = reverse(start, end)
            # 将翻转后结果与原链表相连, 即放回原链表
            pre.next = start
            end.next = after

            pre = end
            curr = end
            start = end.next
        curr = curr.next

    return new_head.next

def demo():
    arr = [1, 2, 3, 4, 5]
    k = 3
    arr = []
    k = 1
    head = list2linkedlist(arr)
    new_head = reverseKGroup(head, k)
    result = linkedlist2list(new_head)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()