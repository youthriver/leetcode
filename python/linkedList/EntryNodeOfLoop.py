
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 链表中环的入口结点 中等
# 给一个长度为n链表，若其中包含环，请找出该链表的环的入口结点，否则，返回null。
# 数据范围：n <= 10000, 1 <= 节点值 <= 10000
# 要求：空间复杂度O(1), 时间复杂度O(n)
# 例如，输入{1,2},{3,4,5}时，对应的环形链表如下图所示：1 -> 2 -> 3 -> 4 -> 5 -> 3
# 可以看到环的入口结点的结点值为3，所以返回结点值为3的结点。
# 输入描述：输入分为2段，第一段是入环前的链表部分，第二段是链表环的部分，后台会根据第二段是否为空将这两段组装成一个无环或者有环单链表
# 返回值描述：返回链表的环的入口结点即可，我们后台程序会打印这个结点对应的结点值；若没有，则返回对应编程语言的空结点即可。
# 示例1: 输入：{1,2},{3,4,5}, 返回值：3, 说明：
# 返回环形链表入口结点，我们后台程序会打印该环形链表入口结点对应的结点值，即3
# 示例2: 输入：{1},{}, 返回值："null", 说明：
# 没有环，返回对应编程语言的空结点，后台程序会打印"null"
# 示例3: 输入：{},{2}, 返回值：2, 说明：
# 环的部分只有一个结点，所以返回该环形链表入口结点，后台程序打印该结点对应的结点值，即2

# 方法一：哈希表法, 遍历链表, 将每个节点存入字典, 如果遇到为空或者当前节点存在字典中则该节点为入环节点
# 方法二：快慢指针, 慢指针每次走一步, 快指针每次走两步, 快慢指针相遇时快指针比慢指针多走了一圈且是慢指针的两倍,
# 假设从起点到入环处距离为x, 慢指针走了环内的长度a, 环的总长度为a+b, 则相遇时慢指针总共走了x+a, 快指针总共走了x+a+b+a,
# 则2*(x+a)=x+a+b+a, 可得x=b,此时第三个指针从链表起始位置开始走, 第三个指针会和慢指针在入环处相遇,
# 此时第三个指针走了x步, 慢指针走了b步

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def list2linkedlist(arr1, arr2):
    head = LinkedList(-1)
    curr = head
    for index, item in enumerate(arr1):
        curr.next = LinkedList(item)
        curr = curr.next
    for index, item in enumerate(arr2):
        curr.next = LinkedList(item)
        curr = curr.next
        if index == 0:
            temp = curr
        if index == len(arr2) - 1:
            curr.next = temp
    return head.next

def entryNodeOfLoop1(head):
    result = None
    temp = {}
    while head:
        if head not in temp:
            temp[head] = 1
            head = head.next
        else:
            result = head
            break
    return result

def entryNodeOfLoop(head):
    slow = head
    fast = head
    result = None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # slow和fast相遇说明存在环结构
            temp = head
            while temp != slow:
                slow = slow.next
                temp = temp.next
            result = temp
            break
    return result

def demo():
    arr1 = [1, 2]
    arr2 = [3, 4, 5]
    # arr1 = [1]
    # arr2 = []
    # arr1 = []
    # arr2 = [2]
    head = list2linkedlist(arr1, arr2)
    node = entryNodeOfLoop(head)
    if node:
        result = node.value
    else:
        result = None
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()