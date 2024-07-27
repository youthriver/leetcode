
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 链表相加(二) 中等
# 假设链表中每一个节点的值都在 0 - 9 之间，那么链表整体就可以代表一个整数。
# 给定两个这种链表，请生成代表两个整数相加值的结果链表。
# 数据范围：0 <= n, m <= 1000000, 链表任意值 0 <= val <= 9
# 要求：空间复杂度O(n), 时间复杂度O(n)
# 例如：链表 1 为 9->3->7，链表 2 为 6->3，最后生成新的结果链表为 1->0->0->0 (937+63=1000)。
# 示例1: 输入：[9,3,7],[6,3], 返回值：{1,0,0,0}
# 示例2: 输入：[0],[6,3], 返回值：{6,3}

# 方法一：将两个链表反转后逐位相加，将相加后的结果链表再次反转即为结果

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
def list2linkedlist(arrs):
    heads = []
    for arr in arrs:
        head = LinkedList(-1)
        curr = head
        for item in arr:
            curr.next = LinkedList(item)
            curr = curr.next
        heads.append(head.next)
    return heads

def linkedlist2list(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result

def reverse(head):
    # 1 -> 2 -> 3, 1 <- 2 - 3, 1 <- 2 <- 3
    curr = head
    post = head.next
    curr.next = None
    while curr and post:
        temp = post.next
        post.next = curr
        curr = post
        post = temp
    return curr

def addInList(heads):
    head1 = reverse(heads[0])
    head2 = reverse(heads[1])
    jinwei = 0
    head = LinkedList(-1)
    curr = head
    while head1 and head2:
        temp = head1.value + head2.value + jinwei
        jinwei = temp // 10
        value = temp % 10
        curr.next = LinkedList(value)
        curr = curr.next
        head1 = head1.next
        head2 = head2.next
    while head1:
        temp = head1.value + jinwei
        jinwei = temp // 10
        value = temp % 10
        curr.next = LinkedList(value)
        curr = curr.next
        head1 = head1.next
    while head2:
        temp = head2.value + jinwei
        jinwei = temp // 10
        value = temp % 10
        curr.next = LinkedList(value)
        curr = curr.next
        head2 = head2.next
    if jinwei > 0:
        curr.next = LinkedList(jinwei)
        curr = curr.next
    head = reverse(head.next)
    return head

def demo():
    arrs = [[9, 3, 7], [6, 3]]
    arrs = [[0], [6, 3]]
    heads = list2linkedlist(arrs)
    node = addInList(heads)
    result = linkedlist2list(node)
    logging.info(f'result is {result}')


if __name__ == '__main__':
    demo()