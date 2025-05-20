
import logging
import os

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 无重复数字的升序数组的二分查找：从升序数组nums中查找目标值target, 存在返回下标, 不存在返回-1, 时间复杂度o(log n), 空间复杂度o(1)

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    index = -1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return index

def demo():
    nums = [-1, 0, 3, 4, 6, 10, 13, 14]  # 6
    target = 13
    nums = []  # -1
    target = 3
    # nums = [-1, 0, 3, 4, 6, 10, 13, 14]  # -1
    # target = 2
    # nums = [0, 1]  # 1
    # target = 1
    result = binary_search(nums, target)
    logging.info('result is {}'.format(result))

if __name__ == '__main__':
    demo()