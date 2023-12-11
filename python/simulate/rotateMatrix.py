
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:[%(message)s]', level=logging.DEBUG)

# 顺时针旋转矩阵  中等
# 有一个NxN整数矩阵, 请编写一个算法, 将矩阵顺时针旋转90度.
# 给定一个NxN的矩阵, 和矩阵的阶数N, 请返回旋转后的NxN矩阵.
# 数据范围: 0<n<300, 矩阵中的值满足0<=val<=1000
# 要求: 空间复杂度O(N^2), 时间复杂度O(N^2)
# 进阶: 空间复杂度O(1), 时间复杂度O(N^2)
# 示例一: 输入 [[1,2,3],[4,5,6],[7,8,9]],3  返回值[[7,4,1],[8,5,2],[9,6,3]]

# 方法一: 原坐标为(x, y)的点顺时针旋转90后变为(y, order-1-x)的坐标, 其中order表示为矩阵阶数
# 此题需要注意的是 在对新的二维列表进行赋值时, 常用的 result=arr,或者result=[[0]*n]*n是创建一个浅拷贝列表,各行表示的是一个地址,
# 所以result[row][col]会改变所有行的第col个元素, 尤其注意

def rotate_matrix1(arr, order):
    result = [[0] * order] * order
    for row in range(order):
        for col in range(order):
            temp = arr[order - 1 - col][row]
            temp1 = result[row][col]
            result[row][col] = temp

    return result

def rotate_matrix(arr, order):
    # 使用列表解析创建一个新的二维列表并赋值
    # 现在list2是对list1的一个深拷贝，改变list2不会影响list1
    result = [row[:] for row in arr]

    for row in range(order):
        for col in range(order):
            temp = arr[order - 1 - col][row]
            # result[row].append(temp)
            result[row][col] = temp

    return result

def demo():
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    order = 3
    result = rotate_matrix(arr, order)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()