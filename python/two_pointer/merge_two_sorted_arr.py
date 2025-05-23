
import logging
import os

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 给出一个有序的整数数组A和有序的整数数组B, 请将数组B合并到数组A中, 变成一个有序的升序数组
# 数组范围: 0 <= n, m <= 100, |A_i| <= 100, |B_i| <= 100
# 注意
# 1. 保证A数组有足够的空间存放B数组的元素, A和B中初始的元素数目分别为m和n, A的数组空间大小为m+n
# 2. 不要返回合并的数组, 将数组B的数据合并到A里面就好了, 且后台会自动将合并后的数组A的内容打印出来, 所以也不需要自己打印
# 3. A数组在[0, m-1]的范围内也是有序的
# [4,5,6][1,2,3] -> [1,2,3,4,5,6]
# [1,2,3][2,5,6] -> [1,2,2,3,5,6]
# 方法: 逆向双指针

def merge(arr1, arr2, m, n):
    left = m - 1
    right = n -1
    index = len(arr1) - 1
    while left >= 0 and right >= 0:
        if arr1[left] <= arr2[right]:
            arr1[index] = arr2[right]
            right -= 1
        else:
            arr1[index] = arr1[left]
            left -= 1
        index -= 1
    while right >= 0:
        arr1[index] = arr2[right]
        right -= 1
        index -= 1

    return arr1

def demo():
    arr1 = [1, 2, 3, 0, 0, 0]
    arr2 = [2, 5, 6]
    # arr1 = [4, 5, 6, 0, 0, 0]
    # arr2 = [1, 2, 3]
    result = merge(arr1, arr2, 3, 3)
    print(result)

if __name__ == '__main__':
    demo()