
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 判断是否为回文字符串
# 给定一个长度为n的字符串, 请编写一个函数判断该字符串是否回文. 如果是回文请返回true, 否则返回false
# 字符串回文指该字符串正序与其逆序逐字符一致.
# 数据范围: 0<=n<=1000000
# 要求: 空间复杂度O(1), 时间复杂度O(n)
# 备注: 字符串长度不大于1000000, 且仅有小写字母组成
# 示例一: 输入 "absba", 返回值true
# 示例二: 输入 "ranko", 返回值false
# 示例三: 输入 "yamatomaya", 返回值false
# 示例四: 输入 "a", 返回值true

def is_palindrome(strs):
    left = 0
    right = len(strs) - 1
    while left <= right:
        if strs[left] != strs[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

def demo():
    strs = 'yamatomaya'
    strs = 'ranko'
    strs = 'absba'
    strs = 'a'
    result = is_palindrome(strs)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()