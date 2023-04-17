class Node():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def preOrder(root):
    if root:
        preOrder(root.left)
        print(root.val)
        preOrder(root.right)




t=Node(1)
t.left=Node(2)
t.right=Node(3)

preOrder(t)


