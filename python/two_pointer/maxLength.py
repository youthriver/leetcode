
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 最长无重复子数组 中等
# 给定一个长度为n的数组arr，返回arr的最长无重复元素子数组的长度，无重复指的是所有数字都不相同。
# 子数组是连续的，比如[1,3,5,7,9]的子数组有[1,3]，[3,5,7]等等，但是[1,3,7]不是子数组
# 数据范围：0 <= arr.length <= 10^5, 0 < arr[i] <= 10^5
# 示例1: 输入：[2,3,4,5], 返回值：4, 说明：[2,3,4,5]是最长子数组
# 示例2: 输入：[2,2,3,4,3], 返回值：3, 说明：[2,3,4]是最长子数组
# 示例3: 输入：[9], 返回值：1
# 示例4: 输入：[1,2,3,1,2,3,2,2], 返回值：3, 说明：最长子数组为[1,2,3]
# 示例5: 输入：[2,2,3,4,8,99,3], 返回值：5, 说明：最长子数组为[2,3,4,8,99]

# 方法一：双指针，注意边界条件！！

def maxLength(arr):
    result = []
    n = len(arr)
    left = 0
    while (left < n):
        item = arr[left]
        temp = {item: left}
        if left + 1 >= n:
            if (len(temp) > len(result)):
                result = temp.keys()
            break
        for right in range(left+1, n, 1):
            if arr[right] not in temp:
                temp[arr[right]] = right
                if right == n - 1:
                    if len(arr[left:right+1]) > len(result):
                        result = arr[left:right+1]
                    left = n
            else:
                if len(arr[left:right]) > len(result):
                    result = arr[left:right]
                left = temp[arr[right]] + 1
                break
    logging.info(f'result is {result}')
    return len(result)

def demo():
    arr = [2, 3, 4, 5]
    arr = [2, 2, 3, 4, 3]
    # arr = [9]
    arr = [1,2,3,1,2,3,2,2]
    arr = [2,2,3,4,8,99,3]
    result = maxLength(arr)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()