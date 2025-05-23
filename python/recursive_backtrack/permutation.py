
import logging
import os

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 给出一组数字, 返回该组数字的所有排列, 例如
# [1, 2, 3] -> [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# [1] -> [[1]]
# 以数字在数组中的位置靠前为优先级, 按字典序排列输出
# 数据范围: 数字个数 0 < n <= 6
# 要求: 空间复杂度o(n!), 时间复杂度o(n!)

# 程序调用自身的编程技巧称为递归（ recursion）。
# 递归做为一种算法在程序设计语言中广泛应用。 一个过程或函数在其定义或说明中有直接或间接调用自身的一种方法，它通常把一个大型复杂的问题层层转化为一个与原问题相似的规模较小的问题来求解，递归策略只需少量的程序就可描述出解题过程所需要的多次重复计算，大大地减少了程序的代码量。
# 通常来说，为了描述问题的某一状态，必须用到该状态的上一个状态；而如果要描述上一个状态，又必须用到上一个状态的上一个状态…… 这样用自己来定义自己的方法就是递归。
# 递归是一种算法结构。递归会出现在子程序中，形式上表现为直接或间接的自己调用自己。典型的例子是阶乘，计算规律为：n!=n×(n−1)!n!=n \times (n-1)!

# 回溯算法实际上一个类似枚举的搜索尝试过程，主要是在搜索尝试过程中寻找问题的解，当发现已不满足求解条件时，就“回溯”返回，尝试别的路径。
# 回溯法是一种选优搜索法，按选优条件向前搜索，以达到目标。但当探索到某一步时，发现原先选择并不优或达不到目标，就退回一步重新选择，这种走不通就退回再走的技术为回溯法。
# 回溯的思路基本如下：当前局面下，我们有若干种选择，所以我们对每一种选择进行尝试。如果发现某种选择违反了某些限定条件，此时 return；如果尝试某种选择到了最后，发现该选择是正确解，那么就将其加入到解集中。
# 在这种思想下，我们需要清晰的找出三个要素：选择 (Options)，限制 (Restraints)，结束条件 (Termination)。
# 回溯是一种算法思想，它是用递归实现的。回溯的过程类似于穷举法，但回溯有“剪枝”功能，即自我判断过程。例如有求和问题，给定有 7 个元素的组合 [1, 2, 3, 4, 5, 6, 7]，求加和为 7 的子集。累加计算中，选择 1+2+3+4 时，判断得到结果为 10 大于 7，那么后面的 5, 6, 7 就没有必要计算了。这种方法属于搜索过程中的优化，即“剪枝”功能。




def permutation(arr):
    if len(arr) <= 1:
        return [arr]
    result = []
    for item in arr:
        temp_input = arr.copy()  ## 不要改变arr
        temp_input.remove(item)
        temps = permutation(temp_input)
        for temp in temps:
            # temp.append(item)
            # result.append(temp)

            aa = [item]
            aa.extend(temp)
            result.append(aa)

    return result

def demo():
    arr = [1, 2, 3]
    # arr = [1]
    # arr = [2, 3]
    result = permutation(arr)
    print(result)

if __name__ == '__main__':
    demo()