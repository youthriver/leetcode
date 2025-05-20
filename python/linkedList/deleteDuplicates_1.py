
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 删除有序链表中重复的元素-I 简单
# 删除给出链表中的重复元素（链表中元素从小到大有序），使链表中的所有元素都只出现一次
# 例如：给出的链表为 1 -> 1 -> 2, 返回 1 -> 2; 给出的链表为  1 -> 1 -> 2 -> 3 -> 3, 返回 1 -> 2 -> 3

# 数据范围：链表长度满足 0 <= n < = 100, 链表中任意节点的值满足 ｜val| <= 100
# 要求：空间复杂度O(1), 时间复杂度O(n)
# 示例1: 输入：{1,1,2}, 返回值：{1,2}
# 示例2: 输入：{}, 返回值：{}

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
def deleteDuplicates_1(head):
    curr = head
    while curr and curr.next:
        temp = curr.next
        while (temp) and (curr.value == temp.value):
            temp = temp.next
        curr.next = temp
        curr = curr.next
    return head

def demo():
    arr = [1, 1, 2]
    arr = []
    head = list2linkedlist(arr)
    head = deleteDuplicates_1(head)
    result = linkedlist2list(head)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()