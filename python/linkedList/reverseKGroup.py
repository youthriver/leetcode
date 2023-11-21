
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

def reverseKGroup(head, k):
    curr = head
    step = 1
    new_head = head
    while curr:
        if step % k == 1:
            slow = curr
        if step % k == 0:
            fast = curr
            if new_head is head:
                new_head = curr
            step = 0
            prev = fast.next
            for i in range(k):
            # while slow is not fast.next:
                nxt = slow.next
                slow.next = prev
                prev = slow
                slow = nxt
            curr = slow
        else:
            curr = curr.next
        step += 1

    return new_head

def demo():
    arr = [1, 2, 3, 4, 5]
    k = 2
    head = list2linkedlist(arr)
    new_head = reverseKGroup(head, k)
    result = linkedlist2list(new_head)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()