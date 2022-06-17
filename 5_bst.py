"""
Binary Search Tree follows a stronger invariant than Heap.
An element in BST is greater than all nodes in its left
subtree and is smaller than all nodes in its right 
subtree

Use BST whenever you want Dynamic Sorting i.e. elements
come and go but you always want a sorted representation
of elements to be available
"""


class Node:

    def __init__(self, key, parent, left, right):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
    
    def __str__(self):
        s = "key: " + str(self.key)
        if self.parent is not None:
            s = s + ", parent: " + str(self.parent.key)
        if self.left is not None:
            s = s + ", left: " + str(self.left.key)
        if self.right is not None:
            s = s + ", right :" + str(self.right.key)
        
        return s


class Tree:

    def __init__(self, root):
        self.root = root
    
    @staticmethod
    def _rec_inorder(node):
        if node is None:
            return
        Tree._rec_inorder(node.left)
        print(node.key, end=" ")
        Tree._rec_inorder(node.right)

    def inorder_traversal(self):
        Tree._rec_inorder(self.root)

    def search(self, val):
        current = self.root
        while current is not None:

            if val == current.key:
                return current
            elif val > current.key:
                current = current.right
            else:
                current = current.left
        
        return None

def build_bst(arr):
    if len(arr) < 1:
        return None

    root = Node(arr[0], None, None, None)
    for i in range(1, len(arr)):
        current = root
        prev = None

        while current is not None:
            is_left_child_of_parent = False
            is_right_child_of_parent = False

            if arr[i] < current.key:
                # go left
                prev = current
                current = current.left
                is_left_child_of_parent = True
            elif arr[i] > current.key:
                # go right
                prev = current
                current = current.right
                is_right_child_of_parent = True

        newNode = Node(arr[i], prev, None, None)

        if is_left_child_of_parent:
            prev.left = newNode
        if is_right_child_of_parent:
            prev.right = newNode

    return Tree(root)


def capture_inputs():
    raw = input()
    return [int(r) for r in raw.split()]


def main():
    arr = capture_inputs()
    tree = build_bst(arr)
    
    print("Inorder traversal ")
    tree.inorder_traversal()

    print("\nEnter value to be searched: ")
    val = int(input())
    found = tree.search(val)
    if found is None:
        print("Value not found!")
    else:
        print("Value found: ", found)   # Node's default __str__ method will fire


if __name__ == "__main__":
    main()
