
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 最长公共子串 中等
# 给定两个字符串str1和str2,输出两个字符串的最长公共子串
# 题目保证str1和str2的最长公共子串存在且唯一。
# 数据范围：0 <= |str1|, |str2| <= 5000
# 要求：空间复杂度O(n^2), 时间复杂度O(n^2)
# 示例1: 输入："1AB2345CD","12345EF", 返回值："2345"

# 方法一：动态规划方法，利用二维矩阵temp记录str1前k1个和str2前k2个子字符串的最长公共字串，如果当前第k1和k2个元素不等，则temp[k1][k2]=0
# 否则，则为temp[k1-1][k2-1]+1，temp的最大值则为最长公共字串的长度str_num，
# 找到最大值所在位置，说明往前数str_num个元素则为最长公共字串

def longestCommonString_1(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    temp = [[False for _ in range(n2+1)] for _ in range(n1+1)]
    str_num = 0
    for index1, item1 in enumerate(str1):
        for index2, item2 in enumerate(str2):
            if (item1 == item2):
                temp[index1+1][index2+1] = temp[index1][index2] + 1
                if temp[index1+1][index2+1] > str_num:
                    str_num = temp[index1+1][index2+1]
            else:
                temp[index1+1][index2+1] = 0
    logging.info(f'temp is {temp}')
    for index1 in range(n1, -1, -1):
        for index2 in range(n2, -1, -1):
            if temp[index1][index2] == str_num:
                row = index1
                col = index2
                break
    if str_num > 0:
        result = str1[row-str_num:row]
    else:
        result = ''
    return result

def demo():
    str1 = '1AB2345CD'
    str2 = '12345EF'
    result = longestCommonString_1(str1, str2)
    logging.info(f'result is {result}')


if __name__ == '__main__':
    demo()