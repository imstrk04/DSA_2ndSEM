class BinaryTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def populate(self):
        print("Enter the root Node:")
        value = int(input())
        self.root = self.Node(value)
        self.populate_helper(self.root)

    def populate_helper(self, node):
        print("Do you want to enter left of", node.value, "? (True/False):")
        left = input().lower() == 'true'
        if left:
            print("Enter the value of the left of", node.value)
            value = int(input())
            node.left = self.Node(value)
            self.populate_helper(node.left)

        print("Do you want to enter right of", node.value, "? (True/False):")
        right = input().lower() == 'true'
        if right:
            print("Enter the value of the right of", node.value)
            value = int(input())
            node.right = self.Node(value)
            self.populate_helper(node.right)

    def display(self):
        self.display_helper(self.root, "")

    def display_helper(self, node, indent):
        if node is None:
            return
        print(indent + str(node.value))
        self.display_helper(node.left, indent + "\t")
        self.display_helper(node.right, indent + "\t")

    def pretty_display(self):
        self.pretty_display_helper(self.root, 0)

    def pretty_display_helper(self, node, level):
        if node is None:
            return
        self.pretty_display_helper(node.right, level + 1)
        if level != 0:
            for i in range(level - 1):
                print("|", end="\t\t")
            print("|------->", node.value)
        else:
            print(node.value)
        self.pretty_display_helper(node.left, level + 1)

    def pre_order(self):
        self.pre_order_helper(self.root)

    def pre_order_helper(self, node):
        if node is None:
            return
        print(node.value, end=" ")
        self.pre_order_helper(node.left)
        self.pre_order_helper(node.right)

    def in_order(self):
        self.in_order_helper(self.root)

    def in_order_helper(self, node):
        if node is None:
            return
        self.in_order_helper(node.left)
        print(node.value, end=" ")
        self.in_order_helper(node.right)

    def post_order(self):
        self.post_order_helper(self.root)

    def post_order_helper(self, node):
        if node is None:
            return
        self.post_order_helper(node.left)
        self.post_order_helper(node.right)
        print(node.value, end=" ")


# Example usage
tree = BinaryTree()
tree.populate()
print("\nDisplay Tree:")
tree.display()

print("\nPretty Display Tree:")
tree.pretty_display()

print("\nPre-Order Traversal:")
tree.pre_order()

print("\nIn-Order Traversal:")
tree.in_order()

print("\nPost-Order Traversal:")
tree.post_order()
