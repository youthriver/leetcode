
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 数字字符串转化成IP地址 中等
# 现在有一个只包含数字的字符串，将该字符串转化成IP地址的形式，返回所有可能的情况。
# 例如：
# 给出的字符串为"25525522135",
# 返回["255.255.22.135", "255.255.221.35"]. (顺序没有关系)
# 数据范围：字符串长度 0 <= n <= 12
# 要求：空间复杂度O(n!), 时间复杂度O(n!)
# 注意：ip地址是由四段数字组成的数字序列，格式如 "x.x.x.x"，其中 x 的范围应当是 [0,255]。
# 示例1: 输入："25525522135", 返回值：["255.255.22.135","255.255.221.35"]
# 示例2: 输入："1111", 返回值：["1.1.1.1"]
# 示例3: 输入："000256", 返回值：[]

def demo():
    arr = []

if __name__ == '__main__':
    demo()