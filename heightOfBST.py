class bst:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
def insert(root,node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left,node)

def height(r):
    if r is None:
        return 0
    else:
        l = height(r.left)
        ri = height(r.right)
        if l>ri:
            return l+1
        else:
            return ri+1
r = bst(20)
[insert(r,bst(int(input()))) for _ in range(10)]
print(height(r)-1)
