
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 螺旋矩阵
# 给定一个m x n 大小的矩阵(m行n列), 按螺旋的顺序返回矩阵中的所有元素
# 数据范围: 0<=n,m<=10, 矩阵中任意元素都满足|val|<=100
# 要求: 空间复杂度O(nm), 时间复杂度O(nm)
# 示例一: 输入[[1,2,3],[4,5,6],[7,8,9]], 返回值[1,2,3,6,9,8,7,4,5]
# 示例二: 输入[], 返回值[]

# 方法一: 按照向右、向下、向左、向上的顺序从外圈遍历, 需要考虑清楚边界条件
# 方法二: 每次去矩阵第一行, 然后将矩阵逆时针旋转90度后再取第一行, 递归处理直到为空

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

def spiralOrder2(matrix):
    '''
    递归法，一行代码。
    [*zip(*matrix)] 表示将 matrix 的第一列作为第一行，第二列作为第二行… 即将矩阵进行对角线对称。
    * 后面加上可迭代对象，相当于将可迭代对象依次列出。
    可以用在两个场合：
    1、[*a] 表示将a变为list，相当于 list(a)
    2、fun(*a) 表示将a变为list，并且每个元素分别作为fun()的一个参数，即这时 fun 被传入了多个参数，而不是一个。
    [*zip(*matrix)][::-1] 表示先将 matrix 进行对角线对称，然后将所有行逆序排列。
    '''
    return matrix and [*matrix.pop(0)] + spiralOrder2([*zip(*matrix)][::-1])

def demo():
    arr = []
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    arr = [[1,2]]
    arr = [[1,2,3],[4,5,6]]
    # result = spiral_order(arr)
    result = spiralOrder2(arr)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()