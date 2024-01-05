class Node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self,value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = Node(value)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = Node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("Value already in Tree")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self,cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value), end = " ")
            self._print_tree(cur_node.right_child)

    def search(self,value):
        if self.root is not None:
            return self._search(value,self.root)
        else:
            return False

    def _search(self,value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._search(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._search(value, cur_node.right_child)

    def find_max(self):
        if self.root is None:
            return None
        return self._find_max(self.root)

    def _find_max(self,cur_node):
        if cur_node.right_child is None:
            return cur_node.value
        return self._find_max(cur_node.right_chld)

    
