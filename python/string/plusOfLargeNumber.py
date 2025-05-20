
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 大数加法 中等
# 以字符串的形式读入两个数字，编写一个函数计算它们的和，以字符串形式返回。
# 数据范围：s.length, t.length <= 100000, 字符串仅由'0'~‘9’构成
# 要求：时间复杂度O(n)
# 示例1: 输入："1","99", 返回值："100", 说明：1+99=100
# 示例1: 输入："114514","", 返回值："114514"

def plusOfLargeNumber(str1, str2):
    result = ''
    n1 = len(str1)
    n2 = len(str2)
    # if (n1 == 0) or (n2 == 0):
    #     return str1 + str2
    if n1 > n2:
        str2 = '0' * (n1 - n2) + str2
    elif n1 < n2:
        str1 = '0' * (n2 - n1) + str1
    jinwei = 0
    for index in range(max(n1, n2)-1, -1, -1):
        temp = int(str1[index]) + int(str2[index]) + jinwei
        jinwei = temp // 10
        temp = temp - jinwei * 10
        result += str(temp)
    if jinwei > 0:
        result += str(jinwei)
    return result[::-1]

def demo():
    str1 = '1'
    str2 = '99'
    str1 = '114514'
    str2 = ''
    result = plusOfLargeNumber(str1, str2)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()