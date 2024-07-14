
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 盛水最多的容器 中等
# 给定一个数组height，长度为n，每个数代表坐标轴中的一个点的高度，height[i]是在第i点的高度，请问，从中选2个高度与x轴组成的容器最多能容纳多少水
# 1.你不能倾斜容器
# 2.当n小于2时，视为不能形成容器，请返回0
# 3.数据保证能容纳最多的水不会超过整形范围，即不会超过2^31-1
# 数据范围：0 <= height.length <= 10^5, 0 <= height[i] <= 10^4
# 如输入的height为[1,7,3,2,4,5,8,2,7]，那么最大面积为[7,3,2,4,5,8,2,7]=7 * (index_8 - index_1)=49
# 示例1: 输入：[1,7,3,2,4,5,8,2,7], 返回值：49
# 示例2: 输入：[2,2], 返回值：2
# 示例3: 输入：[5,4,3,2,1,5], 返回值：25

def demo():
    arr = []

if __name__ == '__main__':
    demo()