

import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 归并排序: O(nlogn)	O(nlogn)	O(nlogn)	O(n)	外部排序	稳定
# 归并排序分为partition和merge两步, 确保左边数组小于等于右边数组

def merge(left, right):
    result = []
    index_left = 0
    index_right = 0
    while (index_left < len(left)) and (index_right < len(right)):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
    while (index_left < len(left)):
        result.append(left[index_left])
        index_left += 1
    while (index_right < len(right)):
        result.append(right[index_right])
        index_right += 1
    return result

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    result = merge(left, right)

    return result


def demo():
    arr = [3, 2, 1]
    arr = []
    arr = [1]
    arr = [1, 2, 3, 4, 5, 6, 7, 0]
    arr = [1, 2, 3]
    result = mergeSort(arr)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()