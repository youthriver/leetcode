
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(level)s: %(message)s', level=logging.DEBUG)

# 数组中只出现一次的两个数字  中等
# 一个整型数组里除了两个数字只出现一次, 其他的数字都出现了两次, 请写程序找出这两个只出现一次的数字.
# 数据范围: 数组长度 2<=n<=1000, 数组中每个数的大小0<val<=1000000
# 要求: 空间复杂度O(1), 时间复杂度O(n)
# 提示: 输出时按非降序排列
# 示例一: 输入[1,4,1,6], 返回值[4, 6], 说明: 返回的结果中较小的数排列在前面
# 示例二: 输入[1,2,3,3,2,9], 返回值[1,9]

def find_nums_appear_once(arr):
    return

def demo():
    arr = []
    result = find_nums_appear_once(arr)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()