
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
    for item in arr:
        temp = TreeNode(item)


def demo():
    pass

if __name__ == '__main__':
    demo()