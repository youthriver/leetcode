
import logging
import os

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 给出一组数字，返回该组数字的所有排列
# [1,2,3] -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# [1] -> [[1]]
# 空间复杂度o(n!), 时间复杂度o(n!)

# 要考虑到数组中有重复数字的情况
# 递归方法 / 非递归方法 - 字典序 (对给定的字符集中的字符规定了一个先后关系，在此基础上规定两个全排列的先后是从左到右逐个比较对应的字符的先后。)
# 如果有重复元素, 则排列总数少于n的阶乘, 可以剪枝进行处理

# 回溯: 前进尝试 + 后退(状态清除更新) + 剪枝(返回条件)

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

def demo():
    arr = [1, 2, 3]
    # arr = [1]
    arr = [1, 1]
    result = full_permutation(arr)
    print(result)

if __name__ == '__main__':
    demo()
