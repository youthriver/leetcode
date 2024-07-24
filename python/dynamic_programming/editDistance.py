
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s:%(message)s', level=logging.DEBUG)

# 编辑距离(一) 较难
# 给定两个字符串 str1 和 str2 ，请你算出将 str1 转为 str2 的最少操作数。
# 你可以对字符串进行3种操作：
# 1.插入一个字符
# 2.删除一个字符
# 3.修改一个字符。
# 数据范围：字符串长度满足 1 <= n <= 1000, 保证字符串中只出现小写英文字母。
# 示例1: 输入："nowcoder","new", 返回值：6, 说明："nowcoder"=>"newcoder"(将'o'替换为'e')，修改操作1次
# "nowcoder"=>"new"(删除"coder")，删除操作5次
# 示例2: 输入："intention","execution", 返回值：5, 说明：一种方案为:
# 因为2个长度都是9，后面的4个后缀的长度都为"tion"，于是从"inten"到"execu"逐个修改即可
# 示例3: 输入："now","nowcoder", 返回值：5

def demo():
    arr = []

if __name__ == '__main__':
    demo()