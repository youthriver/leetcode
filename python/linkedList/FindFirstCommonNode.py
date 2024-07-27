
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 两个链表的第一个公共结点 简单
# 输入两个无环的单向链表，找出它们的第一个公共结点，如果没有公共节点则返回空。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
# 数据范围：n <= 1000
# 要求：空间复杂度O(1), 时间复杂度O(n)
# 例如，输入{1,2,3},{4,5},{6,7}时，两个无环的单向链表的结构如下图所示： 1 -> 2 -> 3 -> 6 -> 7, 4 -> 5 -> 6 -> 7
# 可以看到它们的第一个公共结点的结点值为6，所以返回结点值为6的结点。
# 输入描述：输入分为是3段，第一段是第一个链表的非公共部分，第二段是第二个链表的非公共部分，第三段是第一个链表和第二个链表的公共部分。 后台会将这3个参数组装为两个链表，并将这两个链表对应的头节点传入到函数FindFirstCommonNode里面，用户得到的输入只有pHead1和pHead2。
# 返回值描述：返回传入的pHead1和pHead2的第一个公共结点，后台会打印以该节点为头节点的链表。
# 示例1: 输入：{1,2,3},{4,5},{6,7}, 返回值：{6,7}, 说明：
# 第一个参数{1,2,3}代表是第一个链表非公共部分，第二个参数{4,5}代表是第二个链表非公共部分，最后的{6,7}表示的是2个链表的公共部分
# 这3个参数最后在后台会组装成为2个两个无环的单链表，且是有公共节点的
# 示例2: 输入：{1},{2,3},{}, 返回值：{}, 说明：
# 2个链表没有公共节点 ,返回null，后台打印{}

# 方法一：首先遍历两个链表，分别记录两个链表长度为n1和n2，如果第一个链表和第二个链表的最后一个元素相同，说明有公共部分，
# 重新遍历链表，将较长链表先走abs(n1-n2)步，在两个链表长度相同的情况下继续遍历，出现的第一个相同元素即为第一个公共节点

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def list2linkedlist(arrs):
    heads = []
    head = LinkedList(-1)
    curr = head
    for item in arrs[2]:
        curr.next = LinkedList(item)
        curr = curr.next
    temp = head.next
    for index, arr in enumerate(arrs):
        if index >= 2:
            break
        head = LinkedList(-1)
        curr = head
        for item in arr:
            curr.next = LinkedList(item)
            curr = curr.next
        curr.next = temp
        heads.append(head.next)
    return heads

def linkedlist2list(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result

def findFirstCommonNode(heads):
    head1 = heads[0]
    head2 = heads[1]
    curr1 = head1
    num1 = 0
    curr2 = head2
    num2 = 0
    while curr1:
        num1 += 1
        if curr1.next:
            curr1 = curr1.next
        else:
            break
    while curr2:
        num2 += 1
        if curr2.next:
            curr2 = curr2.next
        else:
            break
    if curr1 != curr2:
        return curr1.next
    curr1 = head1
    curr2 = head2
    if num1 >= num2:
        step = num1 - num2
        for i in range(step):
            curr1 = curr1.next
    else:
        step = num2 - num1
        for i in range(step):
            curr2 = curr2.next
    while curr1 != curr2:
        curr1 = curr1.next
        curr2 = curr2.next
    return curr1

def demo():
    arrs = [[1, 2, 3], [4, 5], [6, 7]]
    arrs = [[1], [2, 3], []]
    heads = list2linkedlist(arrs)
    node = findFirstCommonNode(heads)
    result = linkedlist2list(node)
    logging.info(f'result is {result}')


if __name__ == '__main__':
    demo()