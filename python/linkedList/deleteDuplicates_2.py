
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 删除有序链表中重复的元素-II 中等
# 给出一个升序排序的链表，删除链表中的所有重复出现的元素，只保留原链表中只出现一次的元素。
# 例如：1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5, 返回 1 -> 2 -> 5; 给出的链表为 1 -> 1 -> 1 -> 2 -> 3, 返回 2 -> 3
# 数据范围：链表长度 0 <= n <= 10000, 链表中的值满足 |val| <= 1000
# 要求：空间复杂度O(n), 时间复杂度O(n)
# 进阶：空间复杂度O(1), 时间复杂度O(n)
# 示例1: 输入：{1,2,2}, 返回值：{1}
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

def deleteDuplicates_2(head):
    if (not head) or (not head.next):
        return head
    new_head = LinkedList(head.value - 1)
    curr = head
    prev = new_head
    while curr:
        while (curr and curr.next) and (curr.value == curr.next.value):
            temp = curr.value
            while (curr) and (curr.value == temp):
                curr = curr.next
        prev.next = curr
        prev = prev.next
        if curr:
            curr = curr.next
    return new_head.next
def demo():
    arr = [1, 2, 2]
    arr = []
    arr = [1, 2, 3, 3, 4, 4, 5]
    head = list2linkedlist(arr)
    head = deleteDuplicates_2(head)
    result = linkedlist2list(head)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()