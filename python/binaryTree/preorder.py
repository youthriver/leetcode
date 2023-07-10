
class TreeNode:
    def __init__(self, value):
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
    queue = [root]
    for index, item in enumerate(arr):
        if len(queue) == 0:
            continue
        temp = queue[0]
        if index * 2 + 1 < num and arr[index * 2 + 1]:
            left = TreeNode(arr[index * 2 + 1])
            temp.left = left
            queue.append(left)
        if index * 2 + 2 < num and arr[index * 2 + 2]:
            right = TreeNode(arr[index * 2 + 2])
            temp.right = right
            queue.append(right)
        del queue[0]
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

def preorder_recursive(root):
    result = []
    def trans(node):
        if node:
            result.append(node.value)
            trans(node.left)
            trans(node.right)
    trans(root)
    return result

def preorder(root):
    result = []
    stacks = [root]
    while stacks:
        temp = stacks[0]
        if temp:
            result.append(temp.value)
            stacks.append(temp.left)
            stacks.append(temp.right)
        del stacks[0]
    return result

def demo():
    arr = [3,9,20,None,None,15,7]
    # root = list2tree(arr)
    root = list2tree_recursive(arr)

    result = preorder(root)
    print(result)

if __name__ == '__main__':
    demo()