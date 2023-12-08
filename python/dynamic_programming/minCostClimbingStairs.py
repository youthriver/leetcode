
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 最小花费爬楼梯
# 给定一个整数数组cost, 其中cost[i]是从楼梯第i个台阶向上爬需要支付的费用, 下标从0开始, 一旦你支付此费用, 即可选择向上爬一个或者两个台阶
# 你可以选择从下标为0或者下标为1的台阶开始爬楼梯
# 请你计算并返回到达楼梯顶部的最低花费.
# 数据范围: 数据长度满足1<=n<=10^5, 数组中的值满足1<=cost_i<=10^4
# 示例一: 输入[2,5,20], 返回值5, 说明: 你将从下标为1的台阶开始, 支付5, 向上爬两个台阶, 到达楼梯顶部, 总花费为5
# 示例二: 输入[1,100,1,1,1,90,1,1,80,1], 返回值6,
# 说明: 你将从下标为0的台阶开始, 1. 支付1, 向上爬两个台阶, 到达下标为2的台阶; 2. 支付1, 向上爬两个台阶, 到达下标为4的台阶;
# 3. 支付1, 向上爬两个台阶, 到达下标为6的台阶; 4. 支付1, 向上爬一个台阶, 到达下标为7的台阶;
# 5. 支付1, 向上爬两个台阶, 到达下标为9的台阶; 6. 支付1, 向上爬一个台阶, 到达楼梯顶部. 总花费为6

# 方法一: 动态规划的方法, 到达第n阶台阶有两种方法, 从第n-1阶爬一个台阶或者从n-2阶爬两个台阶,
# 递归公式为:f(n) = min( f(n-1)+cost[n-1], f(n-2)+cost[n-2] )
# 借助一个列表用于存储到达每个节点的最小花费

def min_cost_climbing_stairs(arr):
    n = len(arr)
    result = [0] * (n + 1)
    if n == 0:
        return 0
    if n <= 2:
        return min(arr)
    for i in range(2, n+1):
        result[i] = min(result[i-1]+arr[i-1], result[i-2]+arr[i-2])
    return result[n]

def demo():
    arr = [2,5,20]
    arr = [1,100,1,1,1,90,1,1,80,1]
    result = min_cost_climbing_stairs(arr)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()