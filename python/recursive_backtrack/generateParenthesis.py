
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 括号生成 中等
# 给出n对括号, 请编写一个函数来生成所有的由n对括号组成的合法组合。
# 例如，给出n=3，解集为： "((()))", "(()())", "(())()", "()()()", "()(())"
# 数据范围：0 <= n <= 10
# 要求：空间复杂度O(n), 时间复杂度O(2^n)
# 示例1: 输入：1, 返回值：["()"]
# 示例2: 输入：2, 返回值：["(())","()()"]

# 方法一：括号放置过程中，对于当前位置cur，如果左括号数目小于n则可放置左括号，如果右括号数目小于左括号数目则可放置右括号
# 要保持左括号数目要大于等于右括号数目，小于等于输入数字n，当左括号数目等于输入数字n时，则当前组合已确定，
# 将n_left - n_right个右括号放在队尾，并将当前结果存入result

def generateParenthesis(num):
    def recursive(num, n_left, n_right, temp):
        if (n_left == num) and (n_right == num):
            result.append(temp)
            return
        if (n_left < num):
            recursive(num, n_left + 1, n_right, temp+'(')
        if (n_right < n_left):
            recursive(num, n_left, n_right + 1, temp+')')

    result = []
    n_left = 0
    n_right = 0
    temp = ''
    recursive(num, n_left, n_right, temp)

    return result

def demo():
    num = 3
    num = 0
    num = 1
    num = 2
    result = generateParenthesis(num)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()