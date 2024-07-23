
from collections import OrderedDict

import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 设计LRU缓存结构 较难
# 设计LRU(最近最少使用)缓存结构，该结构在构造时确定大小，假设大小为 capacity ，操作次数是 n ，并有如下功能:
# 1. Solution(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
# 2. get(key)：如果关键字 key 存在于缓存中，则返回key对应的value值，否则返回 -1 。
# 3. set(key, value)：将记录(key, value)插入该结构，如果关键字 key 已经存在，则变更其数据值 value，如果不存在，则向缓存中插入该组 key-value ，如果key-value的数量超过capacity，弹出最久未使用的key-value
# 提示:
# 1.某个key的set或get操作一旦发生，则认为这个key的记录成了最常使用的，然后都会刷新缓存。
# 2.当缓存的大小超过capacity时，移除最不经常使用的记录。
# 3.返回的value都以字符串形式表达，如果是set，则会输出"null"来表示(不需要用户返回，系统会自动输出)，方便观察
# 4.函数set和get必须以O(1)的方式运行
# 5.为了方便区分缓存里key与value，下面说明的缓存里key用""号包裹
# 数据范围：1 <= capacity <= 10^5, 0 <= key, value <= 2 * 10^9, 1 <= n <= 10^5
# 示例1: 输入：["set","set","get","set","get","set","get","get","get"],[[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]],2,
# 返回值：["null","null","1","null","-1","null","-1","3","4"],
# 说明：我们将缓存看成一个队列，最后一个参数为2代表capacity，所以
# Solution s = new Solution(2);
# s.set(1,1); //将(1,1)插入缓存，缓存是{"1"=1}，set操作返回"null"
# s.set(2,2); //将(2,2)插入缓存，缓存是{"2"=2，"1"=1}，set操作返回"null"
# output=s.get(1);// 因为get(1)操作，缓存更新，缓存是{"1"=1，"2"=2}，get操作返回"1"
# s.set(3,3); //将(3,3)插入缓存，缓存容量是2，故去掉某尾的key-value，缓存是{"3"=3，"1"=1}，set操作返回"null"
# output=s.get(2);// 因为get(2)操作，不存在对应的key，故get操作返回"-1"
# s.set(4,4); //将(4,4)插入缓存，缓存容量是2，故去掉某尾的key-value，缓存是{"4"=4，"3"=3}，set操作返回"null"
# output=s.get(1);// 因为get(1)操作，不存在对应的key，故get操作返回"-1"
# output=s.get(3);//因为get(3)操作，缓存更新，缓存是{"3"=3，"4"=4}，get操作返回"3"
# output=s.get(4);//因为get(4)操作，缓存更新，缓存是{"4"=4，"3"=3}，get操作返回"4"

# LRU（Least recently used，最近最少使用）算法根据数据的历史访问记录来进行淘汰数据，
# 其核心思想是“如果数据最近被访问过，那么将来被访问的几率也更高”。
# LRU（The Least Recently Used，最近最久未使用算法）是一种常见的缓存算法

# 方法一：哈希表 + 双向链表的结构实现 LRU 缓存，哈希表中存放key和value, 双向链表中也存放key和value, 不过python不好写
# python 中用 dict+list 实现, 列表记录每个元素调用的时间，最近调用元素放在最后面，dict记录key-value对
# 方法二：python中用 OrderedDict 实现
# python中有一个标准库的类的OrderedDict，该类有以下两个方法用来实现LRU算法就十分简单：
# popitem(last=True)：有序字典的 popitem() 方法移除并返回一个 (key, value) 键值对。 如果 last 值为真，则按 LIFO 后进先出的顺序返回键值对，否则就按 FIFO 先进先出的顺序返回键值对。
# move_to_end(key, last=True)：将现有 key 移动到有序字典的任一端。 如果 last 为真值（默认）则将元素移至末尾；如果 last 为假值则将元素移至开头。如果 key 不存在则会触发 KeyError


class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.recent = []
        self.result = []
        self.num = 0

    def set(self, item):
        key, value = item
        if key in self.cache:
            self.cache[key] = value
            self.recent.remove(key)
            self.recent.append(key)
        elif self.num < self.capacity:
            self.cache[key] = value
            self.num += 1
            self.recent.append(key)
        else:
            del self.cache[self.recent[0]]
            del self.recent[0]
            self.recent.append(key)
            self.cache[key] = value
        self.result.append(None)
    def get(self, item):
        item = item[0]
        if item in self.cache:
            self.result.append(self.cache[item])
            # 最后访问的元素放在列表最后
            if item != self.recent[-1]:
                self.recent.remove(item)
                self.recent.append(item)
        else:
            self.result.append("-1")

class LRU1:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.result = []

    def get(self, item):
        item = item[0]
        if item in self.cache:
            self.result.append(self.cache[item])
            self.cache.move_to_end(item, last=True)
        else:
            self.result.append("-1")

    def set(self, item):
        key, value = item
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        elif len(self.cache) < self.capacity:
            self.cache[key] = value
        else:
            self.cache.popitem(last=False)
            self.cache[key] = value
        self.result.append(None)


def demo():
    operations = ["set", "set", "get", "set", "get", "set", "get", "get", "get"]
    values = [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    capacity = 2
    # lru = LRU(capacity)
    lru = LRU1(capacity)
    for operation, item in zip(operations, values):
        if operation == "set":
            lru.set(item)
        elif operation == "get":
            lru.get(item)
    result = lru.result
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()