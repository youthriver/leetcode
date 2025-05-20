
import logging
logging.basicConfig(format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)

# 验证IP地址  中等
# 编写一个函数来验证输入的字符串是否是有效的IPv4或IPv6地址
# IPv4地址由十进制数和点来表示, 每个地址包含4个十进制数, 其范围为0-255, 用(".")分割. 比如172.16.254.1;
# 同时, IPv4地址内的数不会以0开头. 比如, 地址172.16.254.01是不合法的.
# IPv6地址由8组16进制的数字来表示, 每组表示16比特. 这些组数字通过(":")分割. 比如, 2001:0db8:85a3:0000:0000:8a2e:0370:7334是一个有效的地址,
# 而且, 我们可以加入一些以0开头的数字, 字母可以使用大写, 也可以是小写. 所有, 2001:db8:85a3:0:0:8A2E:0370:7334也是一个有效的IPv6 address
# (即忽略0开头, 忽略大小写).
# 然而, 我们不能因为某个组的值为0, 而使用一个空的组, 以至于出现(::)的情况. 比如, 2001:0db8:85a3::8A2E:0370:7334是无效的IPv6地址.
# 同时, 在IPv6地址中, 多余的0也是不被允许的. 比如, 02001:db8:85a3:0000:0000:8a2e:0370:7334是无效的.
# 说明: 你可以认为给定的字符串里没有空格或者其他特殊字符.
# 数据范围: 字符串长度满足5<=n<=50
# 进阶: 空间复杂度O(n), 时间复杂度O(n)
# 备注: ip地址的类型, 可能为IPv4, IPv6, Neither
# 示例一: 输入 "172.16.254.1", 返回值 "IPv4", 说明: 这是一个有效的IPv4地址, 所有返回"IPv4"
# 示例二: 输入 "2001:db8:85a3:0:0:8A2E:0370:7334", 返回值 "IPv6", 说明: 这是一个有效的IPv6地址, 所有返回"IPv6"
# 示例三: 输入 "256.256.256.256", 返回值 "Neither", 说明: 这个地址既不是IPv4也不是IPv6地址

def is_ipv4(arr):
    parts = arr.split('.')
    if (len(parts) != 4) or ('' in parts):
        return False
    for item in arr:
        # if not item.isdigit():
        if ((item >= 'a' and item <='z') or (item >= 'A' and item <= 'Z')):
            return False

    for part in parts:
        if int(part) >= 255:
            return False
        if ((part.startswith('0')) and (part != '0')):
            return False

    return True

def is_ipv6(arr):
    parts = arr.split(':')
    if (len(parts) != 8) or ('' in parts):
        return False
    for item in arr.lower():
        if (item > 'f' and item <= 'z'):
            return False
    for part in parts:
        if len(part) > 4:
            return False


    return True

def validate_ip(arr):
    if is_ipv4(arr):
        return "IPv4"
    elif is_ipv6(arr):
        return "IPv6"
    return "Neither"

def demo():
    arr = '172.16.254.1'
    result = validate_ip(arr)
    logging.info(f'result is {result}')

if __name__ == '__main__':
    demo()