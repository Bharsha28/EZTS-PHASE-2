class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key
def insert(root,key):
    if root is None:
        return node(key)
    else:
        if root.data==key:
            return root
        elif root.data<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root
def search(root,key):
    if root is None or root.data==key:
        return root
    if root.data <key:
        return search(root.right,key)
    return search(root.left,key)
def inorder(root):
      if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
a=int(input("enter no.of nodes"))

for i in range(a):
    n=int(input("enter node val:"))
    if(i==0):
        r=node(n)
    else:
        r=insert(r,n)
inorder(r)
n=int(input("\nenter an elment to search:"))
n=search(r,n)
if n is not None:
    print("  found")
else:
    print(" not found")
