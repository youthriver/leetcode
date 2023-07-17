
import logging
import os

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 对于一个长度为n的字符串, 做一些变形:
# 首先对于这个字符串包含着一些空格, 就像"Hello World"一样, 我们要做的就是把这个字符串中由空格隔开的单词反序, 同时反转每个字符的大小写
# "Hello World" -> "wORLD hELLO"
# "This is a sample", 16 -> "SAMPLE A IS tHIS"
# "nowcoder", 8 -> "NOWCODER"
# "iOS", 3 -> "Ios"
# 字符串中包含大写英文字母、小写英文字母、空格
# 进阶: 空间复杂度o(n), 时间复杂度o(n)

def string_translate(arr, num):

    return

def demo():
    arr = ''
    num = len(arr)
    result = string_translate(arr, num)
    logging.info(result)


if __name__ == '__main__':
    demo()