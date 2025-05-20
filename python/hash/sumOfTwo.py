
import logging
import os

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 给定一个整形数组numbers和一个目标值target, 找出数组中两个加起来等于目标值的数的下标, 返回的下标按照升序排列
# 保证target一定可以由数组里面的两个数字相加得到
# 空间复杂度O(n), 时间复杂度O(nlogn)
# [3, 2, 4],6 => [1, 2]
# [20, 70, 110, 150], 90 => [0, 1]

def sumOfTwo(arr, target):
    # o(nlogn)
    result = [None, None]
    temp = {}
    for pos, item in enumerate(arr):
        temp[item] = pos

    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == target:
            result[0] = temp[arr[left]]
            result[1] = temp[arr[right]]
            break
        elif (arr[left] + arr[right] > target):
            right = right - 1
        else:
            left = left + 1
    return result


def sumOfTwo_hash(arr, target):
    result = [None, None]
    temp = {}
    for pos, item in enumerate(arr):
        if target - item in temp:
            pos1 = pos
            pos2 = temp[target - item]
            break
        temp[item] = pos
    result[0] = min([pos1, pos2])
    result[1] = max([pos1, pos2])
    return result



def demo():
    arr = [20, 70, 110, 150]
    target = 90
    # arr = [3, 2, 4]
    # target = 6
    # result = sumOfTwo(arr, target)
    result = sumOfTwo_hash(arr, target)
    print(result)

if __name__ == '__main__':
    demo()