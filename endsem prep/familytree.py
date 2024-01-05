from abstracttree import AbstractTree
class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

class FamilyTree(AbstractTree):
    def __init__(self):
        self._root = None
        self._size = 0

    def root(self):
        return self._root

    def parent(self, pos):
        # In a family tree, we don't have a parent reference
        # So, this method will not be implemented
        pass

    def num_children(self, pos):
        node = pos
        return len(node.children)

    def children(self, pos):
        node = pos
        return node.children

    def __len__(self):
        return self._size

    def add_child(self, parent, child_name):
        new_child = TreeNode(child_name)
        parent.children.append(new_child)
        self._size += 1

# Example usage:
family_tree = FamilyTree()

# Adding family members to the tree
family_tree._root = TreeNode("John")

family_tree.add_child(family_tree._root, "Alice")
family_tree.add_child(family_tree._root, "Bob")

alice = family_tree.children(family_tree._root)[0]
bob = family_tree.children(family_tree._root)[1]

family_tree.add_child(alice, "Charlie")
family_tree.add_child(alice, "Daisy")

family_tree.add_child(bob, "Eve")
family_tree.add_child(bob, "Frank")

# Displaying family tree height
print("Family Tree Height:", family_tree.height())  # Output: Family Tree Height: 2
