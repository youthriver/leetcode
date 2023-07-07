
class TreeNode():
    def __int__(self, value):
        self.value = value
        self.left = None
        self.right = None

def createTree():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    b.right = e


def list2tree(arr):
    num = len(arr)
    if num == 0:
        return None
    root = TreeNode(arr[0])
    temp = root
    for index, item in enumerate(arr):
        if index * 2 + 1 < num:
            temp.left = TreeNode(arr[index * 2 + 1])
        if index * 2 + 2 < num:
            temp.right = TreeNode(arr[index * 2 + 2])
    return root


def list2tree_recursive(arr):
    # arr = [3,9,20,None,None,15,7]
    def trans(index):
        if index >= len(arr) or arr[index] == None:
            return None
        if index < len(arr):
            temp = TreeNode(arr[index])
            temp.left = trans(index * 2 + 1)
            temp.right = trans(index * 2  + 2)
        return temp
    root = trans(0)
    return root

def demo():
    pass

if __name__ == '__main__':
    demo()