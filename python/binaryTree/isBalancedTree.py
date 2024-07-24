
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 判断是不是平衡二叉树 简单
# 输入一棵节点数为 n 二叉树，判断该二叉树是否是平衡二叉树。
# 在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
# 平衡二叉树（Balanced Binary Tree），具有以下性质：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。
# 样例解释：[1, 2, 3, 4, 5, 6, 7], 样例二叉树如图，为一颗平衡二叉树, 注：我们约定空树是平衡二叉树。
# 数据范围：n <= 100, 树上节点的val值满足 0 <= val <= 1000
# 要求：空间复杂度O(1), 时间复杂度O(n)
# 输入描述：输入一棵二叉树的根节点
# 返回值描述：输出一个布尔类型的值
# 示例1: 输入：{1,2,3,4,5,6,7}, 返回值：true
# 示例2: 输入：{}, 返回值：true


def demo():
    arr = []

if __name__ == '__main__':
    demo()