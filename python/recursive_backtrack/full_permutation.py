
import logging
import os

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 给出一组数字，返回该组数字的所有排列
# [1,2,3] -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# [1] -> [[1]]
# 空间复杂度o(n!), 时间复杂度o(n!)

def full_permutation(arr):
    def recursive():
        pass


    return

def demo():
    arr = [1, 2, 3]
    result = full_permutation(arr)
    print(result)

if __name__ == '__main__':
    demo()
