# class BinaryTree:
#     def __init__(self, left, value, right):
#         self.left = left
#         self.value = value
#         self.right = right
    
#     @staticmethod
#     def preorder(tree):
#         if tree:
#             print(tree.value, end=" ")
#             BinaryTree.preorder(tree.left)
#             BinaryTree.preorder(tree.right)

#     @staticmethod
#     def makeBinaryTree(inorder: list, postorder: list):
#         try:    
#             root = postorder[-1]
#             split_index = inorder.index(root)

#             inorder_left = inorder[:split_index]
#             inorder_right = inorder[split_index + 1:]
#             post_order_left = postorder[:len(inorder_left)]
#             post_order_right = postorder[len(inorder_left):-1]

#             left_tree = BinaryTree.makeBinaryTree(inorder_left, post_order_left)
#             right_tree = BinaryTree.makeBinaryTree(inorder_right, post_order_right)

#             return BinaryTree(left_tree, root, right_tree)
#         except:
#             return None
        

# n = int(input())
# inorder = [*map(int, input().split())]
# postorder = [*map(int, input().split())]

# tree = BinaryTree.makeBinaryTree(inorder, postorder)
# BinaryTree.preorder(tree)

import sys
sys.setrecursionlimit(int(1e6))

def preorder(inorder_start, inorder_end, postorder_start, postorder_end):
    if inorder_start > inorder_end or postorder_start > postorder_end:
        return
    root = postorder[postorder_end]
    split_index = inorder_dictionary[root]

    left_length = split_index - inorder_start
    right_length = inorder_end - split_index

    print(root, end=" ") # Value

    preorder(inorder_start,
             inorder_start + (left_length - 1),
             postorder_start,
             postorder_start + (left_length - 1)
    ) # Left

    preorder(inorder_end - (right_length - 1),
             inorder_end,
             (postorder_end - 1) - (right_length - 1),
             (postorder_end - 1)
    ) # Right


n = int(input())
inorder = [*map(int, input().split())]
inorder_dictionary = {inorder[index]: index for index in range(n)}
postorder = [*map(int, input().split())]
preorder(0, n-1, 0, n-1)