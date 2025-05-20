
import logging
import os

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)
# 使用两个栈实现一个队列，使用n个元素来完成n次在队列尾部插入整数(push)和n次在队列头部删除整数(pop)的功能。队列中的元素为int类型。
# 保证操作合法，即保证pop操作时队列内已有元素。
# n<=1000
# 存储n个元素的空间复杂度为o(n), 插入与删除的时间复杂度都是o(1)

# ['PSH1', 'PSH2' 'POP', 'POP'] => 1,2
# 'PSH1'代表将1插入队列尾部, 'PSH2'代表将2插入队列尾部, 'POP'代表删除一个元素, 先进先出返回1, 'POP'代表删除一个元素, 先进先出返回2

# ['PSH2', 'POP', 'PSH1', 'POP'] => 2, 1

# 队列: 先进先出
# 栈: 先进后出

class Queue:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def inqueue(self, val):
        self.stackA.append(val)

    def dequeue(self):
        if len(self.stackB) > 0:
            result = self.stackB.pop()
        elif len(self.stackA) > 0:
            while len(self.stackA) > 0:
                tmp = self.stackA.pop()
                self.stackB.append(tmp)
            result = self.stackB.pop()
        else:
            result = None

        return result

def stack2queue(arr):
    temp = Queue()
    result = []
    for item in arr:
        if item.startswith('PSH'):
            val = str(item[3::])
            temp.inqueue(val)
        elif item.startswith('POP'):
            result.append(temp.dequeue())

    return result

def demo():
    arr = ['PSH1', 'PSH2', 'POP', 'POP']
    arr = ['PSH2', 'POP', 'PSH1', 'POP']
    result = stack2queue(arr)
    print(','.join(result))

if __name__ == '__main__':
    demo()
