
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 给一个长度为n的数组, 数组中有一个数字出现的次数超过数组长度的一半, 请找出这个数字.
# 例如输入一个长度为9的数组[1,2,3,2,2,2,5,4,2], 由于数字2在数组中出现了5次, 超过数组长度的一半, 因此输出2.
# 数据范围: n<=50000, 数组中元素的值0<=val<=10000
# 要求: 空间复杂度O(1), 时间复杂度O(n), 输入保证数组输入非空, 且保证有解
# 示例1: 输入[1,2,3,2,2,2,5,4,2], 返回值2
# 示例2: 输入[3,3,3,3,2,2,2], 返回值3
# 示例3: 输入[1], 返回值1

def moreThanHalfNum_dict(arr):
    return

def moreThanHalfNum_partition(arr):
    # 利用快排思想, O(n)
    return

def moreThanHalfNum_time():
    # 利用抵消的方法
    return


def demo():
    arr = []
    result = moreThanHalfNum_dict(arr)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()