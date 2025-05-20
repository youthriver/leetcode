
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 跳台阶
# 一只青蛙一次可以跳上1级台阶, 也可以跳上2级. 求该青蛙跳上一个n级的台阶总共有多少种跳法(先后次序不同算不同的结果)
# 数据范围: 1<=n<=40
# 要求: 时间复杂度O(n), 空间复杂度O(1)
# 示例一: 输入2, 返回值2, 说明: 青蛙要跳上二级台阶有两种跳法, 分别是: 先跳一级, 再跳一级或者直接跳两级, 因此答案为2
# 示例二: 输入7, 返回值21

def jumpFloor(num):
    if num == 1:
        return 1
    if num == 2:
        return 2
    f_1 = 1
    f_2 = 2
    for i in range(3, num + 1):
        f_n = f_1 + f_2
        f_1 = f_2
        f_2 = f_n
    return f_n

def demo():
    arr = 7
    result = jumpFloor(arr)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()