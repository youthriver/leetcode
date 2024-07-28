
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 旋转数组的最小数字 简单
# 有一个长度为 n 的非降序数组，比如[1,2,3,4,5]，将它进行旋转，即把一个数组最开始的若干个元素搬到数组的末尾，变成一个旋转数组，
# 比如变成了[3,4,5,1,2]，或者[4,5,1,2,3]这样的。请问，给定这样一个旋转数组，求数组中的最小值。
# 数据范围：1 <= n <= 10000, 数组中任意元素的值: 0 <= val <= 10000
# 要求：空间复杂度O(1), 时间复杂度O(logn)
# 示例1: 输入：[3,4,5,1,2], 返回值：1
# 示例2: 输入：[3,100,200,3], 返回值：3

# [3,-1, 0, 1, 2], [3, 4, 5, 1, 2]
# 方法一：二分查找，初始化left = 0, right = n - 1, 计算中间坐标值mid,
# 将arr[mid]与左边界或右边界相比，有大于小于等于三种情况, 以左边界为例：
# 当 arr[left] > arr[mid]: 此时最小值在[left, mid]之间, 将right置为mid
# 当 arr[left] < arr[mid]: 此时最小值在[mid+1, right]之间, 将left置为mid+1
# 当 arr[left] == arr[mid]: 此时不能确定最小值在哪边, 将left置为left+1缩小搜索范围

# [2, 1] [2, 0, 1, 1, 1]
def minNumberInRotateArray(arr):
    n = len(arr)
    if n < 0:
        return None
    left = 0
    right = n - 1
    while (left < right) and (arr[left] >= arr[right]):
        mid = (right - left + 1) // 2 + left
        if (arr[left] > arr[mid]):
            right = mid
        elif (arr[left] < arr[mid]):
            left = mid + 1
        else:
            left = left + 1

    return arr[left]

def demo():
    arr = [3, 4, 5, 1, 2]
    arr = [3, 100, 200, 3]
    arr = [2, 1]
    arr = [2, 2]
    result = minNumberInRotateArray(arr)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()