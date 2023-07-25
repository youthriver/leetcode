
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 将一个节点数为size链表m位置到n位置之间的区间反转, 要求时间复杂度为o(n), 空间复杂度为o(1)
# 例如: 给出的链表为 1 -> 2 -> 3 -> 4 -> 5 -> NULL, m=2, n=4, 返回 1 -> 4 -> 3 -> 2 -> 5 -> NULL
# 数据范围: 链表长度 0 < size <= 1000, 0 < m <= n <= size, 链表中每个节点的值满足 |val| <= 1000
# 要求: 时间复杂度o(n), 空间复杂度o(n)
# 进阶: 时间复杂度o(n), 空间复杂度o(1)
# 示例1: 输入 {1, 2, 3, 4, 5}, 2, 4, 返回值{1, 4, 3, 2, 5}
# 示例2: 输入 {5}, 1, 1, 返回值{5}


def createLinkedList(arr):
    return

def reverseLinkedList_fromMtoN(linkedlist, m, n):
    return

def demo():
    arr = [1, 2, 3, 4, 5]
    m = 2
    n = 4
    linkedlist = createLinkedList(arr)
    result = reverseLinkedList_fromMtoN(linkedlist, m, n)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()