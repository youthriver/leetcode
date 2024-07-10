

import logging
import os

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 数组中的逆序对 中等
# 在数组中的两个数字, 如果前面一个数字大于后面的数字, 则这两个数字组成一个逆序对. 输入一个数组, 求出这个数组中的逆序对的总数P.
# 并将P对1000000007取模的结果输出, 即输出P mod 1000000007.
# 数据范围: 对于50%的数据, size <= 10^4, 对于100%的数据, size <= 10^5, 数组中所有数字的值满足0<=val<=10^9
# 要求: 空间复杂度O(n), 时间复杂度O(nlogn)
# 输入: 题目保证输入的数组中没有相同的数字
# 示例一: 输入[1, 2, 3, 4, 5, 6, 7, 0], 返回值7
# 示例二: 输入[1, 2, 3], 返回值0

# 逆序对的数目可以标识一个数组和有序数组之间的距离，逆序对的数目越少，数组变成有序数组的步数就越少；逆序对越多，原数组变成有序数组就需要更多的步骤。
# 对于一个有序的数组而言，逆序对的数目就是 0，而一个完全逆序的数组，逆序对的数目当然也就最多
# 方法一: 暴力法, 两层循环遍历, 时间复杂度O(n^2), 空间复杂度O(1)
# 方法二: 拷贝该数组后对拷贝的数组排序。计算数组中的最小值在原始数组中出现的位置，统计原始数组中最小值前面的个数，之后在原始数组中去掉最小值。重复上述步骤。
# 方法三: 基于分治思想的归并排序, 将有序列表和逆序对计数一同返回的递归解法, 把数据分成前后两个数组(递归分到每个数组仅有一个数据项)。合并数组，合并时，出现前面的数组值array[i]大于后面数组值array[j]时；则前面数组array[i]~array[mid]都是大于array[j]的，count += mid+1 - i

def merge(left, right, cnt):
    result = []
    index_left = 0
    index_right = 0
    while (index_left < len(left)) and (index_right < len(right)):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            cnt += len(left) - index_left  # ****
            result.append(right[index_right])
            index_right += 1
    while (index_left < len(left)):
        result.append(left[index_left])
        index_left += 1
    while (index_right < len(right)):
        result.append(right[index_right])
        index_right += 1
    return (result, cnt)

def mergeSort(arr):
    cnt = 0
    if len(arr) < 2:
        return (arr, cnt)
    mid = len(arr) // 2
    left, cnt_left = mergeSort(arr[:mid])
    right, cnt_right = mergeSort(arr[mid:])
    sortArray, cnt = merge(left, right, cnt_left+cnt_right)
    return (sortArray, cnt)

def inversePairs(arr):
    sortArray, result = mergeSort(arr)
    return result % 1000000007

def demo():
    arr = [1, 2, 3, 4, 5, 6, 7, 0]
    arr = [1, 2, 3]
    result = inversePairs(arr)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()