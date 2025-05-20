
import logging
import os

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# https://blog.csdn.net/u011608357/article/details/36933337
# https://blog.csdn.net/sinat_29957455/article/details/113815399

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class ListNode2:
    def __init__(self,val,next=None):
        if isinstance(val,int):
            self.val = val
            self.next = next
        elif isinstance(val,list):
            self.val = val[0]
            self.next = None
            head = self
            for i in range(1,len(val)):
                node = ListNode(val[i])
                head.next = node
                head = head.next


def create2linkedlist():
    head = ListNode(1)  # 测试代码
    p1 = ListNode(2)  # 建立链表1->2->3->4->None;
    p2 = ListNode(3)
    p3 = ListNode(4)
    head.next = p1
    p1.next = p2
    p2.next = p3
    return head

def list2linkedlist(arr):
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        node = ListNode(arr[i])
        curr.next = node
        curr = curr.next
    return head



def reverseLinkedList(head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def reverseLinkedList_recursive(head):
    if head == None or head.next == None:
        return head
    new_head = reverseLinkedList_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head

if __name__ == '__main__':
    # head = create2linkedlist()
    arr = [1, 2, 3, 4]
    head = list2linkedlist(arr)
    # while head:
    #     logging.info(head.val)
    #     head = head.next
    # new = reverseLinkedList(head)
    new = reverseLinkedList_recursive(head)
    while new:
        logging.info(new.val)
        new = new.next