
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 数组中只出现一次的两个数字  中等
# 一个整型数组里除了两个数字只出现一次, 其他的数字都出现了两次, 请写程序找出这两个只出现一次的数字.
# 数据范围: 数组长度 2<=n<=1000, 数组中每个数的大小0<val<=1000000
# 要求: 空间复杂度O(1), 时间复杂度O(n)
# 提示: 输出时按非降序排列
# 示例一: 输入[1,4,1,6], 返回值[4, 6], 说明: 返回的结果中较小的数排列在前面
# 示例二: 输入[1,2,3,3,2,9], 返回值[1,9]

# 方法一: 利用字典的方法
# 方法二: 利用位运算, 异或的方法, 对于只有一个数字出现一次, 其他数字出现两次的数字, 将所有元素异或一遍得到的结果即为出现一次的数字
# 对于本题, 只有两个数字出现一次, 其他的数字都出现两次的列表, 异或一遍后的结果即为两个出现一次的数字的异或结果, 且因两个数字不相同, 结果中至少一位数字为1, 记作index位置的数字为1
# 按照index位是否为1将列表中所有数字分为两组, 每组的异或结果即为出现一次的数字

# 0 异或 x = x, x 异或 x = 0
# bin(x)将x转为二进制表示, a^b表示 a 异或 b
# 原码表示法规定：用符号位和数值表示带符号数，正数的符号位用“0”表示，负数的符号位用“1”表示，数值部分用二进制形式表示。
# 反码表示法规定：正数的反码与原码相同，负数的反码为对该数的原码除符号位外各位取反。
# 补码表示法规定：正数的补码与原码相同，负数的补码为对该数的原码除符号位外各位取反，然后在最后一位加1

def find_nums_appear_once_hash(arr):
    result = []
    temp = {}
    for item in arr:
        if item not in temp:
            temp[item] = 1
        else:
            temp[item] += 1
    for key, value in temp.items():
        if value == 1:
            result.append(key)

    return result

def find_nums_appear_once_bit(arr):
    temp = 0
    for item in arr:
        temp ^= item
    index = 0
    while ((temp>>index) & 1 == 0):
        index += 1
    # 将x与-x进行与操作得到为1的最低位数字, 比如 将 3&(-3)=0011&(1101)=0001,
    # 其中-3用二进制表示为: -3的原码表示为1011, 反码表示为1100, 补码为1101
    # index = temp & (-temp)
    result = [0, 0]
    for item in arr:
        if ((item>>index) & 1 == 0):
            result[0] ^= item
        else:
            result[1] ^= item

    return result

def demo():
    arr = [1, 2, 3, 3, 2, 9]
    # result = find_nums_appear_once_hash(arr)
    result = find_nums_appear_once_bit(arr)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()