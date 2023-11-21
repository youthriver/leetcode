
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 螺旋矩阵
# 给定一个m x n 大小的矩阵(m行n列), 按螺旋的顺序返回矩阵中的所有元素
# 数据范围: 0<=n,m<=10, 矩阵中任意元素都满足|val|<=100
# 要求: 空间复杂度O(nm), 时间复杂度O(nm)
# 示例一: 输入[[1,2,3],[4,5,6],[7,8,9]], 返回值[1,2,3,6,9,8,7,4,5]
# 示例二: 输入[], 返回值[]

def spiral_order(arr):
    result = []
    m = len(arr)
    if m == 0:
        return []
    n = len(arr[0])
    flag = 1
    x_min = 0
    x_max = m - 1
    y_min = 0
    y_max = n - 1
    x = 0
    y = 0
    while (x >= x_min) and (x <= x_max) and (y >= y_min) and (y <= y_max):
        result.append(arr[x][y])
        if flag == 1 and y == y_max:
            flag = 2
            x_min += 1
        elif flag == 2 and x == x_max:
            flag = 3
            y_max -= 1
        elif flag == 3 and y == y_min:
            flag = 4
            x_max -= 1
        elif flag ==4 and x == x_min:
            flag = 1
            y_min += 1
        if flag == 1:
            y += 1
        elif flag == 2:
            x += 1
        elif flag == 3:
            y -= 1
        elif flag == 4:
            x -= 1

    return result

def demo():
    arr = []
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    arr = [[1,2]]
    arr = [[1,2,3],[4,5,6]]
    result = spiral_order(arr)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()