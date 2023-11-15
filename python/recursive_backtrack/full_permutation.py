
import logging
import os

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 给出一组数字，返回该组数字的所有排列
# 以数字在数组中的位置靠前为优先级, 按字典序排列输出
# [1,2,3] -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# [1] -> [[1]]
# 空间复杂度o(n!), 时间复杂度o(n!)

# 要考虑到数组中有重复数字的情况
# 递归方法 / 非递归方法 - 字典序 (对给定的字符集中的字符规定了一个先后关系，在此基础上规定两个全排列的先后是从左到右逐个比较对应的字符的先后。)
# 如果有重复元素, 则排列总数少于n的阶乘, 可以剪枝进行处理

# 回溯: 前进尝试 + 后退(状态清除更新) + 剪枝(返回条件)
# 字典序: 当前排列与下一排列有最长的公共前缀, 两个排列的前k项相同, 则第k+1项大的排列在k+1项小的排列的后面
# 步骤是1. 从右向左找到第一个降序的数, 2. 找到比降序数大的最右边的一个数, 3. 将这两个数字交换位置, 4. 将从左往右第一个数后面的数全部逆序排列, 逆序的目的是使右侧数字按照字典序排列
# 比如 346987521, 1.找到从右往左第一个降序的数6, 2.找到比降序数大的最右边的一个数7, 3.将这两个数交换位置得到347986521, 4.将第一个位置后面的数全部逆序排列得到347125689,
# 则346987521的下一个字典序排列为347125689


# list赋值时是赋值形参地址, 如果函数里面list值改变会导致原数组值改变

def full_permutation(arr):
    def recursive(state, selected):
        if len(state) == len(selected):
            result.append(list(state))
        # 每次遍历时保证相同的元素只遍历一次
        duplicate = set()
        for index, item in enumerate(arr):
            if selected[index] is True:
                continue
            if item in duplicate:
                continue
            duplicate.add(item)
            state.append(item)
            selected[index] = True
            recursive(state, selected)
            state.pop()
            selected[index] = False
    result = []
    state = []
    selected = [False] * len(arr)
    recursive(state, selected)

    return result

def dict_permutation(arr):
    n = len(arr)
    def dict_sort(tmp):
        i = -1
        for i in range(n-2, -1, -1):
            if tmp[i] < tmp[i+1]:
                break
        if (i == -1) or (tmp[i] >= tmp[i+1]):
            return False
        for j in range(n-1, i, -1):
            if tmp[j] > tmp[i]:
                break
        flag = tmp[j]
        tmp[j] = tmp[i]
        tmp[i] = flag
        if i + 1 < n - 1:
            part = tmp[i+1::]
            part.sort()
            tmp[i+1::] = part
        result.append(tmp)
        return True
    arr.sort()
    tmp = arr.copy()
    result = [arr]
    while dict_sort(tmp):
        tmp = result[-1].copy()

    return result

def demo():
    arr = [1, 2, 3]
    arr = [1]
    arr = [1, 1]
    # result = full_permutation(arr)
    result = dict_permutation(arr)
    print(result)

if __name__ == '__main__':
    demo()
