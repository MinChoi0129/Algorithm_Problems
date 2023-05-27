class BinaryTree:
    def __init__(self, left, value, right):
        self.left = left
        self.value = value
        self.right = right


def 전위순회(tree):
    if tree:
        print(tree.value, end="")
        전위순회(tree.left)
        전위순회(tree.right)


def 중위순회(tree):
    if tree:
        중위순회(tree.left)
        print(tree.value, end="")
        중위순회(tree.right)


def 후위순회(tree):
    if tree:
        후위순회(tree.left)
        후위순회(tree.right)
        print(tree.value, end="")


n = int(input())
trees = {
    chr(ascii_num): BinaryTree(None, chr(ascii_num), None)
    for ascii_num in range(65, 65 + 26)
}

for _ in range(n):
    value, left, right = input().split()
    if left != ".":
        trees[value].left = trees[left]
    if right != ".":
        trees[value].right = trees[right]

전위순회(trees["A"])
print()
중위순회(trees["A"])
print()
후위순회(trees["A"])
print()
