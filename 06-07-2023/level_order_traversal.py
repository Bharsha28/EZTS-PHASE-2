class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key
def level_order(root):
    queue=[root]
    while len(queue)!=0:
        ele=queue.pop(0)
        if ele.left!=None:
            queue.append(ele.left)
        if ele.right!=None:
            queue.append(ele.right)
        print(ele.data,end=" ")
root=node(100)
root.left=node(400)
root.right=node(500)
root.left.left=node(700)
root.left.right=node(600)
root.left.right.left=node(900)
root.right.left=node(800)
root.right.right=node(200)
root.right.right.left=node(300)
print("level_order \n")
a=level_order(root)
