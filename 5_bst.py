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
        s = "key= " + str(self.key)
        if self.parent is not None:
            s = s + ", parent=" + str(self.parent.key)
        if self.left is not None:
            s = s + ", left=" + str(self.left.key)
        if self.right is not None:
            s = s + ", right=" + str(self.right.key)

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

    def successor(self, val):
        """
        Successor is also known as "next larger"

        Two cases here:
        1. When the node has right subtree then successor is 
            min value from this right subtree
        2. When the node has no right subtree then the successor
            is that parent of this node which has any left child
        """
        found = self.search(val)
        if found is None:
            return None

        if found.right is not None:
            # Right subtree exists,
            # find min from this sub tree
            rnode = found.right
            while rnode.left is not None:
                rnode = rnode.left
            return rnode
        else:
            # Right subtree does not exist,
            # keep following parent pointers
            # till you find a node which is left
            # child of its parent. That's the
            # successor
            if found.parent is None:
                # basically asking for successor of a root node
                # and when the root has no right subtree
                return None

            while found.parent is not None and \
                    found != found.parent.left:
                found = found.parent
            
            if found.parent is None:
                return None
            elif found == found.parent.left:
                return found.parent
            else:
                return found

    def predecessor(self, val):
        """
        Finds the next smaller node compared to the given value

        1. If there is left subtree then the max from that is the predecessor
        2. If there is no left subtree then go to parent till a node is there
            which is right child of its parent
        """
        found = self.search(val)
        if found is None:
            return None

        if found.left is not None:
            curr = found.left
            prev = found
            while curr is not None:
                prev = curr
                curr = curr.right
            return prev
        else:
            curr = found
            if curr.parent is None:
                return None

            while curr.parent is not None and \
                    curr != curr.parent.right:
                curr = curr.parent
            
            if curr.parent is None:
                return None
            elif curr.parent.right == curr:
                return curr.parent
            else:
                return curr

    def delete(self, val):
        node = self.search(val)
        if node is None:
            raise Exception("Node to be deleted is not found!")

        # if it is leaf node then just kill it!
        if node.left is None and node.right is None:
            if node.parent is not None and node.parent.left == node:
                # if the node was left child of its parent
                node.parent.left = None
            elif node.parent is not None and node.parent.right == node:
                # node is right child of its parent
                node.parent.right = None

            # if we just deleted the root node then set the self.root ptr accordingly
            if node == self.root:
                self.root = None
            del node

        else:
            # intermediate node, just replace with successor's key
            succ = self.successor(val)
            node.key = succ.key
            if succ.parent.left == succ:
                succ.parent.left = succ.right
                if succ.right is not None:
                    succ.right.parent = succ.parent
                del succ
            elif succ.parent.right == succ:
                succ.parent.right = succ.right
                if succ.right is not None:
                    succ.right.parent = succ.parent
                del succ


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
        # Node's default __str__ method will fire
        print("Value found: ", found)

    succ = tree.successor(val)
    print("Successor: ", succ)

    pred = tree.predecessor(val)
    print("Predecessor: ", pred)

    tree.delete(val)
    print("\nInorder traversal after deleting node with value ", val)
    tree.inorder_traversal()


if __name__ == "__main__":
    main()
