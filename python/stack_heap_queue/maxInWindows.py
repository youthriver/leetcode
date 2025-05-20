
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 滑动窗口的最大值 较难
# 给定一个长度为n的数组num和滑动窗口的大小size，找出所有滑动窗口里数值的最大值。
# 例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为[4,4,6,6,6,5];
# 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个{[2,3,4],2,6,2,5,1}, {2,[3,4,2],6,2,5,1}, {2,3,[4,2,6],2,5,1},
# {2,3,4,[2,6,2],5,1}, {2,3,4,2,[6,2,5],1}, {2,3,4,2,6,[2,5,1]}
# 窗口大于数组长度或窗口长度为0的时候，返回空。
# 数据范围：1<=n<=10000,0<=size<=10000, 数组中每个元素的值满足|val|<=10000
# 要求：空间复杂度O(n), 时间复杂度O(n)
# 示例一： 输入[2,3,4,2,6,2,5,1], 3，返回值[4,4,6,6,6,5]
# 示例二：输入[9,10,9,-7,-3,8,2,-6], 5, 返回值[10,10,9,8]
# 示例三：输入[1,2,3,4], 5, 返回值[]

# 维护一个长度为size的排序数组, 用双向队列实现(两端都可弹出元素)，
# 具体实现：当维护的排序数组不为空，且新加入元素大于等于队尾元素时，原队尾元素弹出，直到新加入元素小于队尾元素或维护的排序数组为空
# 当队首元素下标index值小于窗口左侧left时，意味着当前队首元素不在滑动窗口内，需要弹出
# 维护的排序数组存储下标值

def maxInWindows(arr, size):
    if (size > len(arr)) or (size == 0):
        return []
    temp = []
    result = []
    for index in range(len(arr)):
        right = index
        left = right + 1 - size
        if (len(temp) > 0) and (temp[0] < left):
            temp.pop(0)
        if (len(temp) == 0) or (arr[index] < arr[temp[-1]]):
            temp.append(index)
        else:
            while (len(temp) > 0) and (arr[index] >= arr[temp[-1]]):
                temp.pop()
            temp.append(index)

        if left >= 0:
            result.append(arr[temp[0]])
    return result

def demo():
    arr = [2, 3, 4, 2, 6, 2, 5, 1]
    size = 3
    arr = [9, 10, 9, -7, -3, 8, 2, -6]
    size = 5
    arr = [1, 2, 3, 4]
    size = 5
    result = maxInWindows(arr, size)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()