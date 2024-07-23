import heapq
from collections import defaultdict, OrderedDict
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 设计LFU缓存结构 较难
# 一个缓存结构需要实现如下功能。
# set(key, value)：将记录(key, value)插入该结构
# get(key)：返回key对应的value值
# 但是缓存结构中最多放K条记录，如果新的第K+1条记录要加入，就需要根据策略删掉一条记录，然后才能把新记录加入。这个策略为：在缓存结构的K条记录中，哪一个key从进入缓存结构的时刻开始，被调用set或者get的次数最少，就删掉这个key的记录；
# 如果调用次数最少的key有多个，上次调用发生最早的key被删除
# 这就是LFU缓存替换算法。实现这个结构，K作为参数给出
# 数据范围：0 < k <= 10^5, |val| <= 2 * 10^9
# 要求：get和set的时间复杂度都是O(logn), 空间复杂度O(n)
# 若opt=1，接下来两个整数x, y，表示set(x, y)
# 若opt=2，接下来一个整数x，表示get(x)，若x未出现过或已被移除，则返回-1
# 对于每个操作2，返回一个答案
# 示例1: 输入：[[1,1,1],[1,2,2],[1,3,2],[1,2,4],[1,3,5],[2,2],[1,4,4],[2,1]],3, 返回值：[4,-1]
# 说明：在执行"1 4 4"后，"1 1 1"被删除。因此第二次询问的答案为-1
# 备注：1 <= k <= 10^5, -2 * 10^9 <= x, y <= 2 * 10^9

# next() 返回迭代器的下一个项目。next() 函数要和生成迭代器的iter() 函数一起使用。
# iter()函数实际上就是调⽤了可迭代对象的 iter ⽅法。list、tuple等都是可迭代对象

# LFU（Least Frequently Used ，最近最少使用算法）也是一种常见的缓存算法。
# heapq 库是Python标准库之一，提供了构建小顶堆的方法和一些对小顶堆的基本操作方法(如入堆，出堆等)，可以用于实现堆排序算法。参考：https://blog.csdn.net/weixin_43790276/article/details/107741332
# 方法一：小顶堆+哈希表，借用heapq实现(heapq.heappush(heap, num), heapq.heappush(heap, num))，二顶堆是二叉树结构, 只能删除最小元素，中间元素没有提供删除方法
# 方法二：字典+列表
# 方法三：有序字典+列表
# 需要有个字典记录 key-value，还需要一个结构记录调用次数和调用时间

class LFU:
    def __init__(self, k):
        self.k = k
        self.temp = {}
        self.key2time = {}
        self.heapq = []
        self.num = 0
        self.result = []
    def set(self, item):
        key, value = item[1:]
        if key in self.temp:
            self.temp[key] = value
            self.key2time[key] += 1
            time = self.key2time[key]
            self.heapq.remove((time - 1, key))
            heapq.heappush(self.heapq, (time, key))
        elif self.num < self.k:
            self.temp[key] = value
            self.key2time[key] = 1
            time = self.key2time[key]
            heapq.heappush(self.heapq, (time, key))
            self.num += 1
        else:
            _, del_key = heapq.heappop(self.heapq)
            del self.temp[del_key]
            del self.key2time[del_key]
            self.temp[key] = value
            self.key2time[key] = 1
            heapq.heappush(self.heapq, (key, 1))

    def get(self, item):
        key = item[1]
        if key in self.temp:
            self.result.append(self.temp[key])
            time = self.key2time[key]
            self.heapq.remove((time, key))
            heapq.heappush(self.heapq, (time+1, key))
            self.key2time[key] = time + 1
        else:
            self.result.append(-1)

class LFU2:
    def __init__(self, k):
        self.k = k
        self.temp = {}
        self.key2time = {}
        self.time2key = {}
        self.num = 0
        self.min_time = 0
        self.result = []
    def set(self, item):
        key, value = item[1:]
        if key in self.temp:
            self.temp[key] = value
            self.key2time[key] += 1
            time = self.key2time[key]
            self.time2key[time - 1].remove(key)
            if len(self.time2key[time - 1]) == 0:
                self.time2key.pop(time - 1)
                if self.min_time == time - 1:
                    self.min_time = time
            if time not in self.time2key:
                self.time2key[time] = []
            self.time2key[time].append(key)
        elif self.num < self.k:
            self.temp[key] = value
            self.key2time[key] = 1
            time = self.key2time[key]
            if time not in self.time2key:
                self.time2key[time] = []
            self.time2key[time].append(key)
            self.min_time = time
            self.num += 1
        else:
            del_key = self.time2key[self.min_time].pop(0)
            if len(self.time2key[self.min_time]) == 0:
                self.time2key.pop(self.min_time)
            self.temp.pop(del_key)
            self.key2time.pop(del_key)
            self.temp[key] = value
            self.key2time[key] = 1
            time = self.key2time[key]
            if time not in self.time2key:
                self.time2key[time] = []
            self.time2key[time].append(key)
            self.min_time = time

    def get(self, item):
        key = item[1]
        if key in self.temp:
            self.result.append(self.temp[key])
            self.key2time[key] += 1
            time = self.key2time[key]
            self.time2key[time - 1].remove(key)
            if len(self.time2key[time - 1]) == 0:
                self.time2key.pop(time - 1)
                if self.min_time == time - 1:
                    self.min_time = time
            if time not in self.time2key:
                self.time2key[time] = []
            self.time2key[time].append(key)
        else:
            self.result.append(-1)

class LFU3:
    def __init__(self, k):
        self.k = k
        self.temp = {}
        self.key2time = {}
        self.time2key = defaultdict(OrderedDict)
        self.num = 0
        self.min_time = 0
        self.result = []
    def set(self, item):
        key, value = item[1:]
        if key in self.temp:
            self.temp[key] = value
            self.key2time[key] += 1
            time = self.key2time[key]
            self.time2key[time - 1].pop(key)
            if not self.time2key[time - 1]:
                del self.time2key[time - 1]
                if self.min_time == time - 1:
                    self.min_time = time
            self.time2key[time][key] = 1
        elif self.num < self.k:
            self.temp[key] = value
            self.num += 1
            self.key2time[key] = 1
            time = self.key2time[key]
            self.time2key[time][key] = 1
            self.min_time = time
        else:
            del_key, _ = self.time2key[self.min_time].popitem(last=False)
            del self.temp[del_key]
            del self.key2time[del_key]
            self.temp[key] = value
            self.key2time[key] = 1
            if not self.time2key[self.min_time]:
                del self.time2key[self.min_time]
            self.min_time = 1
    def get(self, item):
        key = item[1]
        if key in self.temp:
            self.result.append(self.temp[key])
            self.key2time[key] += 1
            time = self.key2time[key]
            self.time2key[time - 1].pop(key)
            if not self.time2key[time - 1]:
                del self.time2key[time - 1]
                if self.min_time == time - 1:
                    self.min_time = time
            self.time2key[time][key] = 1
        else:
            self.result.append(-1)

def demo():
    arr = [[1, 1, 1], [1, 2, 2], [1, 3, 2], [1, 2, 4], [1, 3, 5], [2, 2], [1, 4, 4], [2, 1]]
    k = 3
    lfu = LFU(k)
    for index, item in enumerate(arr):
        logging.info(f'index is {index}, item is {item}')
        if item[0] == 1:
            lfu.set(item)
        elif item[0] == 2:
            lfu.get(item)
    result = lfu.result
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()