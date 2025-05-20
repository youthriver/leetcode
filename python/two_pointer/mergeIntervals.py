
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 合并区间  中等
# 给出一组区间, 请合并所有重叠的区间.
# 请保证合并后的区间按区间起点升序排列.
# 数据范围: 区间组数0<=n<=2*10^5, 区间内的值都满足0<=val<=2*10^5
# 要求: 空间复杂度O(n), 时间复杂度O(nlogn)
# 进阶: 空间复杂度O(val), 时间复杂度O(val)
# 示例一: 输入[[10,30],[20,60],[80,100],[150,180]], 返回值[[10,60],[80,100],[150,180]]
# 示例二: 输入[[0,10],[10,20]], 返回值[[0,20]]

def merge_intervals(arr):
    result = []
    arr.sort(key=lambda item: item[0])
    # num = len(arr)
    for index, item in enumerate(arr):
        if index == 0:
            result.append(item)
        else:
            if item[0] <= result[-1][1]:
                result[-1][1] = item[1]
            else:
                result.append(item)
    return result

def demo():
    arr = [[10,30],[20,60],[80,100],[150,180]]
    arr = [[0,10],[10,20]]
    result = merge_intervals(arr)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()