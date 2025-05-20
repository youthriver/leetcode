
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 合并k个已排序的链表 较难
# 合并 k 个升序的链表并将结果作为一个升序的链表返回其头节点。
# 数据范围：节点总数 0 <= n <= 5000, 每个节点的val满足 |val| <= 1000
# 要求：时间复杂度O(nlogn)
# 示例1: 输入：[{1,2,3},{4,5,6,7}], 返回值：{1,2,3,4,5,6,7}
# 示例2: 输入：[{1,2},{1,4,5},{6}], 返回值：{1,1,2,4,5,6}

# set不能通过下标访问，必要时可以转化为list访问
# 方法一：遍历各个链表，寻找最小值，放入新的排序链表
# 方法二：分治，每2个链表进行合并，最后合为一个链表

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def list2linkedlist(arr):
    head = LinkedList(-1)
    curr = head
    for index, item in enumerate(arr):
        curr.next = LinkedList(item)
        curr = curr.next
    return head.next

def mergeKLists(heads):
    new_head = LinkedList(-1)
    curr = new_head
    while len(heads) > 0:
        index_list = []
        min_value = None
        min_index = -1
        for index, item in enumerate(heads):
            if item:
                if (not min_value) or (item.value < min_value):
                    min_value = item.value
                    min_index = index
            else:
                index_list.append(index)
        if min_value:
            curr.next = LinkedList(min_value)
            heads[min_index] = heads[min_index].next
            curr = curr.next
        for item in index_list:
            heads.pop(item)


    return new_head.next

def linkedlist2list(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result

def demo():
    arr = [{1, 2, 3}, {4, 5, 6, 7}]
    arr = [{1, 2}, {1, 4, 5}, {6}]
    heads = []
    for index, item in enumerate(arr):
        head = list2linkedlist(list(item))
        heads.append(head)
    head = mergeKLists(heads)
    result = linkedlist2list(head)
    logging.info(f'result is {result}')


if __name__ == '__main__':
    demo()