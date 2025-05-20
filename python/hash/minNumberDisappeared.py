
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 缺失的第一个正整数 中等
# 给定一个无重复元素的整数数组nums，请你找出其中没有出现的最小的正整数
# 进阶：空间复杂度O(1)，时间复杂度O(n)
# 数据范围：-2^31 <= nums[i] <= 2^31 - 1, 0 <= len(nums) <= 5*10^5
# 示例一：输入[1, 0, 2], 返回值3
# 示例二：输入[-2, 3, 4, 1, 5], 返回值2
# 示例三：输入[4, 5, 6, 8, 9], 返回值1

# 对于长度为n的数组，如果不存在缺失的正整数，所有元素value可以放在index=value-1的位置，因此遍历数组，将大于0小于n+1的value值放在value-1位置处，再遍历数组，第一个arr[value-1]!=value处的index+1值即为最终答案
# 方法一：(可处理有重复元素数组，空间复杂度O(n)), 用0初始化一个同样长度为n的数组，遍历输入数组，对于每一个值大于0小于n+1的value，将初始化数组中index=value-1处元素置为1，最后检测初始化数组中从index=0开始的第一个出现0的位置即为答案
# 方法二：(不可处理重复元素，空间复杂度O(1))，遍历数组，对于每个大于0小于n+1的value，将该元素与arr[value-1]位置元素进行交换，使得value值在arr[value-1]处，最后检测从index=0开始第一个index!=arr[index]的位置，index+1即为答案

def minNumberDisappeared(nums):
    n = len(nums)
    index = 0
    while index < len(nums):
        item = nums[index]
        if (item > 0) and (item < n + 1) and (nums[item - 1] != item):
            nums[index] = nums[item - 1]
            nums[item - 1] = item
        else:
            index += 1
    logging.info(f'nums is {nums}')
    result = n + 1
    for index, item in enumerate(nums):
        if item - 1 != index:
            result = index + 1
            break
    return result

def demo():
    nums = [1, 0, 2]
    # nums = [-2, 3, 4, 1, 5]
    # nums = [4, 5, 6, 8, 9]
    # nums = [10, 9, 8, 7, 6, 5, 0, 4, 2, 1, -1]
    result = minNumberDisappeared(nums)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()