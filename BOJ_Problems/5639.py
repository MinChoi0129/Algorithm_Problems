import sys
sys.setrecursionlimit(10000)

class DoubleLinkedList:
    def __init__(self, left, item, right):
        self.left = left
        self.item = item
        self.right = right

def insert_node(node, item):
    if node is None: return DoubleLinkedList(None, item, None)
    elif item < node.item: node.left = insert_node(node.left, item)
    elif item > node.item: node.right = insert_node(node.right, item)
    return node

def postorder(root):
    if root: postorder(root.left); postorder(root.right); print(root.item)

root = None
while True:
    try: root = insert_node(root, int(input()))
    except: break

postorder(root)