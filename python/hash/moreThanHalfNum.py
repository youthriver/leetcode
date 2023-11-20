
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 给一个长度为n的数组, 数组中有一个数字出现的次数超过数组长度的一半, 请找出这个数字.
# 例如输入一个长度为9的数组[1,2,3,2,2,2,5,4,2], 由于数字2在数组中出现了5次, 超过数组长度的一半, 因此输出2.
# 数据范围: n<=50000, 数组中元素的值0<=val<=10000
# 要求: 空间复杂度O(1), 时间复杂度O(n), 输入保证数组输入非空, 且保证有解
# 示例1: 输入[1,2,3,2,2,2,5,4,2], 返回值2
# 示例2: 输入[3,3,3,3,2,2,2], 返回值3
# 示例3: 输入[1], 返回值1

# 方法一: 利用字典, 返回出现次数最多的元素  空间复杂度o(n), 时间复杂度o(n)
# 方法二: 利用快排中partition函数, 找到排列在n/2的元素
# 方法三: 利用抵消的方法, 众数出现的次数比其他所有元素加一起出现次数还要多  空间复杂度o(1), 时间复杂度o(n)

def moreThanHalfNum_dict(arr):
    temp = {}
    max_time = 0
    for item in arr:
        if item in temp:
            temp[item] += 1
        else:
            temp[item] = 1
        if temp[item] > max_time:
            result = item
    return result


def partition(arr, left, right):
    # 每次使得index右边的元素大于等于arr[index], index左边的元素小于等于arr[index]
    pivot = arr[left]
    while left < right:
        while (left < right) and (arr[right] >= pivot):
            right -= 1
        arr[left] = arr[right]
        while (left < right) and (arr[left] <= pivot):
            left += 1
        arr[right] = arr[left]
    arr[left] = pivot

    return left
def moreThanHalfNum_partition(arr):
    # 利用快排思想, O(n)
    n = len(arr)
    left = 0
    right = n - 1
    index = partition(arr, left, right)
    while (index != n//2):
        if index < n//2:
            left = index + 1
            index = partition(arr, left, right)
        else:
            right = index - 1
            index = partition(arr, left, right)
    result = arr[index]
    return result

def moreThanHalfNum_time(arr):
    # 利用抵消的方法: 众数出现的次数比其他所有数字出现的次数还要多
    result = -1
    time = 0
    for item in arr:
        if item == result:
            time += 1
        elif time == 0:
            result = item
            time += 1
        else:
            time -= 1

    return result


def demo():
    arr = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    # result = moreThanHalfNum_dict(arr)
    # result = moreThanHalfNum_time(arr)
    result = moreThanHalfNum_partition(arr)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()