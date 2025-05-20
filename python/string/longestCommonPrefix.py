
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 最长公共前缀
# 给你一个大小为n的字符串数组strs, 其中包含n个字符串, 编写一个函数来查找字符串数组中的最长公共前缀, 返回这个公共前缀
# 数据范围: 0<=n<=5000, 0<=len(strs_i)<=5000
# 进阶: 空间复杂度O(1), 时间复杂度O(n*len)
# 示例一: 输入['abca', 'abc', 'abca', 'abca', 'abc', 'abcc'], 返回值'abc'
# 示例二: 输入['abc'], 返回值'abc'

def longestCommonPrefix(arr):
    num = len(arr)
    if num < 1:
        return None
    prefix = arr[0]
    for item in arr:
        n1 = len(prefix)
        n2 = len(item)
        n = min(n1, n2)
        for i in range(n):
            if prefix[i] != item[i]:
                prefix = prefix[:i]
                break

    return prefix


def demo():
    arr = ['abca', 'abc', 'abca', 'abca', 'abc', 'abcc']
    arr = ['abc']
    result = longestCommonPrefix(arr)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()