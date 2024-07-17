
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 最长公共子序列(二) 中等
# 给定两个字符串str1和str2，输出两个字符串的最长公共子序列。如果最长公共子序列为空，则返回"-1"。目前给出的数据，仅仅会存在一个最长的公共子序列
# 数据范围：0 <= |str1|, |str2| <= 2000
# 要求：空间复杂度O(n^2), 时间复杂度O(n^2)
# 示例1: 输入："1A2C3D4B56","B1D23A456A", 返回值："123456"
# 示例2: 输入："abc","def", 返回值："-1"
# 示例3: 输入："abc","abc", 返回值："abc"
# 示例4: 输入："ab","", 返回值："-1"

# 方法一：首先利用动态规划借助于二维长度矩阵计算出最长公共字串的长度，然后从二维长度矩阵的右下角出发寻找公共字串中的元素，倒序输出即为最后结果

def longestCommonString(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    temp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    curr = ''
    for index1, item1 in enumerate(str1):
        for index2, item2 in enumerate(str2):
            if item1 == item2:
                temp[index1+1][index2+1] = max(temp[index1][index2] + 1, temp[index1+1][index2], temp[index1][index2+1])
            else:
                temp[index1 + 1][index2 + 1] = max(temp[index1][index2], temp[index1 + 1][index2],
                                                       temp[index1][index2 + 1])
    logging.info(f'the max length is {temp[-1][-1]}')
    index1 = n1
    index2 = n2
    while (index1 > 0) and (index2 > 0):
        if str1[index1 - 1] == str2[index2 - 1]:
            curr += str1[index1 - 1]
            index1 -= 1
            index2 -= 1
        else:
            if temp[index1 -1][index2] > temp[index1][index2 - 1]:
                index1 -= 1
            else:
                index2 -= 1
    logging.info(f'curr is {curr}')
    if temp[-1][-1] > 0:
        result = curr[::-1]
    else:
        result = '-1'
    return result

def demo():
    str1 = '1A2C3D4B56'
    str2 = 'B1D23A456A'
    # str1 = 'abc'
    # str2 = 'def'
    str1 = 'abc'
    str2 = 'abc'
    str1 = 'abc'
    str2 = ''
    result = longestCommonString(str1, str2)
    logging.info(f'result is {result}')


if __name__ == '__main__':
    demo()