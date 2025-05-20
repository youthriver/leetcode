
import logging
import os

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)


# 包含min函数的栈
# 定义栈的数据结构, 请在该类型中实现一个能够得到栈中所含最小元素的min函数, 输入操作时保证pop、top和min函数操作时, 栈中一定有元素.
# 此栈包含的方法有: push(value):将value压入栈中, pop():弹出栈顶元素, top():获取栈顶元素, min():获取栈中最小元素
# 数据范围: 操作数量满足0<=n<=300, 输入的元素满足|val|<=10000
# 进阶: 栈的各个操作的时间复杂度是O(1), 空间复杂度是O(n)
# 示例: 输入["PSH-1","PSH2","MIN","TOP","POP","PSH1","TOP","MIN"],输出: -1,2,1,-1
# 解析: "PSH-1"表示将-1压入栈中, 栈中元素为-1; "PSH2"表示将2压入栈中, 栈中元素为2, -1; "MIN"表示获取此时栈中最小元素, 返回-1;
#      "TOP"表示获取栈顶元素, 返回2; "POP"表示弹出栈顶元素, 弹出2, 栈中元素为-1; "PSH1"表示将1压入栈中, 栈中元素为1, -1;
#      "TOP"表示获取栈顶元素, 返回1; "MIN"表示获取此时栈中最小元素, 返回-1;
# 示例1: 输入["PSH-1","PSH2","MIN","TOP","POP","PSH1","TOP","MIN"], 返回值: -1,2,1,-1

# 栈: 先进后出, 队列: 先进先出
# 思路一: 利用一个副栈, 栈顶始终为当前栈内的最小值, 新push元素时, 判断副栈中栈顶与新元素大小, 副栈中push进入二者较小值, pop操作时, 将副栈栈顶元素同时pop
# 思路二: 借用一个变量, 记录当前位置的最小值, 每次push新元素时与最小值进行判断, 如果大于等于最小值则正常push, 小于最小值就先将该最小值先push入栈, 然后将该新元素push入栈, 同时更新最小值,
#        pop元素时, 将pop出的元素与最小值进行判断, 如果大于最小值, 则正常pop, 如果等于最小值, 则在第一次pop后, 将第二次pop的元素用于更新最小值

class Stack_two:
    def __init__(self):
        self.stacks = []
        # 用于记录当前位置的最小值
        self.stacksB = []
    def _push(self, value):
        self.stacks.append(value)
        if (len(self.stacksB) > 0) and (value > self.stacksB[-1]):
            self.stacksB.append(self.stacksB[-1])
        else:
            self.stacksB.append(value)
    def _pop(self):
        self.stacks.pop()
        self.stacksB.pop()
    def _top(self):
        return self.stacks[-1]
    def _min(self):
        return self.stacksB[-1]


class Stack_one:
    def __init__(self):
        self.stacks = []
        self.min = None
    def _push(self, value):
        if self.min is None:
            self.min = value
            self.stacks.append(self.min)
            self.stacks.append(value)
        elif value >= self.min:
            self.stacks.append(value)
        else:
            self.stacks.append(self.min)
            self.stacks.append(value)
            self.min = value
    def _pop(self):
        temp = self.stacks.pop()
        if temp == self.min:
            self.min = self.stacks.pop()

    def _top(self):
        return self.stacks[-1]
    def _min(self):
        return self.min

def stack_with_min(arr):
    # temp = Stack_two()
    temp = Stack_one()
    result = []
    for item in arr:
        if item.startswith('PSH'):
            temp._push(int(item[3::]))
        elif item.startswith('MIN'):
            result.append(str(temp._min()))
        elif item.startswith('TOP'):
            result.append(str(temp._top()))
        elif item.startswith('POP'):
            temp._pop()
    logging.info(f'result is {result}')
    result = ','.join(result)

    return result

def demo():
    arr = ["PSH-1","PSH2","MIN","TOP","POP","PSH1","TOP","MIN"]
    result = stack_with_min(arr)
    logging.info(f'result is {result}')


if __name__ == '__main__':
    demo()