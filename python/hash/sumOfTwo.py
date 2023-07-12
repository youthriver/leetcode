
import logging
import os

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 给定一个整形数组numbers和一个目标值target, 找出数组中两个加起来等于目标值的数的下标, 返回的下标按照升序排列
# 保证target一定可以由数组里面的两个数字相加得到
# 空间复杂度O(n), 时间复杂度O(nlogn)
# [3, 2, 4],6 => [1, 2]
# [20, 70, 110, 150], 90 => [0, 1]

def sumOfTwo(arr, target):
    position = {}
    temp = {}
    for pos, item in enumerate(arr):
        temp[item] = pos

    arr.sort()
            
    return

def demo():
    arr = []
    target = 10
    result = sumOfTwo(arr, target)
    print(result)

if __name__ == '__main__':
    demo()