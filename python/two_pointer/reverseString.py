
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 反转字符串 入门
# 写出一个程序，接受一个字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）
# 数据范围：0 <= n <= 1000
# 要求：空间复杂度O(n), 时间复杂度O(n)
# 示例1: 输入："abcd", 返回值："dcba"
# 示例1: 输入："", 返回值：""

def reverseString1(str):
    return str[::-1]

def reverseString(str):
    result = ''
    n = len(str)
    for index in range(n):
        result += str[n-1-index]
    return result

def demo():
    str = 'abcd'
    result = reverseString(str)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()