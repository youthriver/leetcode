
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 字符串的排列 中等
# 输入一个长度为n的字符串，打印出该字符串中字符的所有排列，你可以以任意顺序返回这个字符串数组。
# 例如输入字符串ABC,则输出由字符A,B,C所能排列出来的所有字符串ABC,ACB,BAC,BCA,CBA和CAB。
# 数据范围：n < 10,
# 要求：空间复杂度O(n!), 时间复杂度O(n!)
# 输入描述：输入一个字符串,长度不超过10,字符只包括大小写字母。
# 示例1: 输入："ab", 返回值：["ab","ba"], 说明：返回["ba","ab"]也是正确的
# 示例2：输入："aab", 返回值：["aab","aba","baa"]
# 示例3：输入："abc"，返回值：["abc","acb","bac","bca","cab","cba"]
# 示例4：输入：""，返回值：[""]

# 递归：通常来说，为了描述问题的某一状态，必须用到该状态的上一个状态；而如果要描述上一个状态，又必须用到上一个状态的上一个状态…… 这样用自己来定义自己的方法就是递归。
# 回溯：当前局面下，我们有若干种选择，所以我们对每一种选择进行尝试。如果发现某种选择违反了某些限定条件，此时 return；如果尝试某种选择到了最后，发现该选择是正确解，那么就将其加入到解集中。

# 方法一：从前往后进行全排列，假设只有第一位的情况下，结果为当前字符；对于n位情况，所有排列可能为将第n位字符分别插入n-1位全排列结果中的各个位置,
# 即假设n-1=2位结果为['ab', 'ba']，则n=3位全排列结果为将第n位元素'c'分别插入'ab'和'ba', 其中插入位置为0->(n-1),即'c'插入'ab'的第0位为'cab',
# 'c'插入'ab'的第1位为'acb', 'c'插入'ab'的第2位为'abc',同理'c'插入'ba'的第0位为'cba', 'c'插入'ba'的第1位为'bca','c'插入'ba'的第2位为'bac',
# 对于重复元素的问题需要考虑当前插入的元素与当前插入位置的元素是否相同，如果相同则跳过
# 方法二：考虑深度优先搜索所有排列方案，即通过字符交换，先固定第1位的字符(n种情况)，再固定第2位字符(n-1种情况)，...，最后固定最后一位字符(1种情况)
# 当字符串存在重复字符时，排列方案中也存在重复的排列方案。为了排除重复方案，需在固定某位字符时，保证“每种字符只在此位固定一次”，即遇到重复字符时不交换，
# 直接跳过。从DFS角度看，此操作称为”剪枝“

def permutationOfString(str):
    n = len(str)
    str = ('').join(sorted(str))
    result = []
    for index in range(n):
        if index == 0:
            result = [str[index]]
        else:
            temp = result
            result = []
            for item in temp:
                for i in range(index + 1):
                    # 剪枝
                    if (i >= len(item)) or (str[index] != item[i]):
                        result.append(item[:i] + str[index] + item[i:])

    return result

def demo():
    str = 'ab'
    # str = ''
    # str = 'abc'
    # str = 'aab'
    result = permutationOfString(str)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()