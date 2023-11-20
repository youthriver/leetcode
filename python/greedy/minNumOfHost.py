
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 有n个活动即将举办, 每个活动都有开始时间与活动的结束时间, 第i个活动的开始时间是start_i, 第i个活动的结束时间是end_i, 举办某个活动就需要为该活动准备一个活动主持人.
# 一位活动主持人在同一时间只能参与一个活动, 并且活动主持人需要全程参与活动, 换句话说, 一个主持人参与了第i个活动, 那么该主持人在(start_i,end_i)
# 这个时间段不能参与其他任何活动. 求为了成功举办这n个活动, 最少需要多少名主持人.
# 数据范围: 1<=n<=10^5, -2^32 <= start_i <= end_i <= 2^31 - 1
# 复杂度要求: 时间复杂度O(nlogn), 空间复杂度O(n)
# 备注: 在int范围内
# 示例一: 输入 2, [[1,2],[2,3]], 返回值1, 说明: 只需要一个主持人就能成功举办这俩个活动
# 示例二: 输入 2, [[1,3],[2,4]], 返回值2, 说明: 需要两个主持人才能成功举办这俩个活动

# ？？？？没想明白
# 方法一: 将开始、结束时间分别排序, 遍历开始时间, 如果小于当前结束时间, 主持人数目加一, 否则当前结束时间变为下一个

def minNumOfHost(arr):
    # 将数组分别按照开始、结束时间排序
    arr.sort(key=lambda x: (x[0], x[1]))
    num = len(arr)
    starts = []
    ends = []
    for i in range(num):
        starts.append(arr[i][0])
        ends.append(arr[i][1])
    result = -1
    index_end = 0
    for i in range(num):
        if starts[i] < ends[index_end]:
            result += 1
        else:
            index_end += 1

    return result

def demo():
    arr = [[1,3],[2,4]]
    arr = [[1,2],[2,3]]
    # arr = [[1, 5], [2, 3], [4, 6]]  # 返回2
    result = minNumOfHost(arr)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()