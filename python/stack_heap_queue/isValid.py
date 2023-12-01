
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(level)s: %(message)s', level=logging.DEBUG)

# 有效括号序列  简单
# 给出一个仅包含字符 '(', ')', '{', '}', '[', ']', 的字符串, 判断给出的字符串是否是合法的括号序列
# 括号必须以正确的顺序关闭, "()", "()[]{}"都是合法的括号序列, 但"(]"和"([}]"不合法
# 数据范围: 字符串长度 0<=n<=10000
# 要求: 空间复杂度O(n), 时间复杂度O(n)
# 示例一: 输入 "[", 返回值 false
# 示例二: 输入 "[]", 返回值 true

def is_valid(arr):
    return

def demo():
    arr = '['
    result = is_valid(arr)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()