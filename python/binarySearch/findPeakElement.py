
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s:[%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 寻找峰值 中等
# 给定一个长度为n的数组nums, 请你找到峰值并返回其索引. 数组可能包含多个峰值, 在这种情况下, 返回任何一个所在位置即可.
# 1. 峰值元素是指其值严格大于左右相邻值的元素. 严格大于即不能有等于
# 2. 假设 nums[-1] = nums[n] = 负无穷
# 3. 对于所有有效的 i 都有 nums[i] != nums[i + 1]
# 4. 你可以使用 O(log N) 的时间复杂度实现此问题吗?
# 数据范围: 1 <= nums.length <= 2 * 10^5, -2^31 <= nums[i] <= 2^31 - 1
# 如输入[2,4,1,2,7,8,4]时, 会形成两个山峰, 一个是索引为1, 峰值为4的山峰, 另一个是索引为5, 峰值为8的山峰
# 示例一: 输入[2,4,1,2,7,8,4], 返回值1, 说明: 4和8都是峰值元素, 返回4的索引1或者8的索引5都可以
# 示例二: 输入[1,2,3,1], 返回值2, 3是峰值元素, 返回其索引2

# 方法一: 可以采用在非排序数组中找最大值的思想, 最大值一定是峰值, 每次查找需选择一个非递增序列, (递增序列不存在峰值), 可以选择其中的较大值

def find_peak_element(arr):
    left = 0
    num = len(arr)
    right = num - 1
    result = 0
    while (left < right):
        # 如果二分查找加上等号会员什么影响
        mid = (left + right) // 2
        if mid == 0:
            low = -float('inf')
        else:
            low = arr[mid - 1]
        if mid == num - 1:
            high = -float('inf')
        else:
            high = arr[mid + 1]
        if (arr[mid] > low) and (arr[mid] > high):
            result = mid
            break
        elif low > high:
            right = mid - 1
        else:
            left = mid + 1

    return result

def demo():
    arr = [2, 4, 1, 2, 7, 8, 4]
    arr = [1, 2, 3, 1]
    arr = [1]
    arr = [1, 2, 3]
    arr = [2, 1]
    result = find_peak_element(arr)
    logging.info(f'result is {result}')


if __name__ == '__main__':
    demo()