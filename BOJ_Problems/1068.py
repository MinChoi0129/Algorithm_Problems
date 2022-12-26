class DoubleLinkedList:
    def __init__(self, left, node_num, right):
        self.left, self.right = left, right
        self.node_num, self.parent = node_num, None
    def addChildRelation(self, node):
        if self.left is None: self.left = node; node.parent = self
        elif self.right is None: self.right = node; node.parent = self
        else: raise Exception("No place to add child node")
    def free(self):
        if self.left is not None: self.left.free()
        if self.right is not None: self.right.free()
        p = self.parent
        if p:
            if p.left is self: p.left = None
            elif p.right is self: p.right = None
        self.left = self.right = self.node_num = self.parent = None
class Tree:
    def __init__(self, number_of_nodes, parent_of_nodes):
        self.tree_space = {}
        for child_idx in range(number_of_nodes):
            parent_idx = parent_of_nodes[child_idx]
            try:
                child = self.tree_space[child_idx]
                try: # 자식o, 부모o
                    parent = self.tree_space[parent_idx]
                    parent.addChildRelation(child)
                except: # 자식o, 부모x
                    if parent_idx != -1:
                        new_parent = DoubleLinkedList(None, parent_idx, None)
                        new_parent.addChildRelation(child)
                        self.tree_space[parent_idx] = new_parent
            except:
                try: # 자식x, 부모o
                    parent = self.tree_space[parent_idx]
                    new_child = DoubleLinkedList(None, child_idx, None)
                    parent.addChildRelation(new_child)
                    self.tree_space[child_idx] = new_child
                except: # 자식x, 부모x
                    new_child = DoubleLinkedList(None, child_idx, None)
                    self.tree_space[child_idx] = new_child
                    if parent_idx != -1:
                        new_parent = DoubleLinkedList(None, parent_idx, None)
                        new_parent.addChildRelation(new_child)
                        self.tree_space[parent_idx] = new_parent
    def removeNode(self, node_num): self.tree_space[node_num].free()  
    def getLeafNodes(self): return [node for node in self.tree_space.values() if (node.node_num is not None and node.left is None and node.right is None)]

n, parent_indices, delete_node_number = int(input()), [*map(int, input().split())], int(input())
tree = Tree(n, parent_indices)
tree.removeNode(delete_node_number)
print(len(tree.getLeafNodes()))