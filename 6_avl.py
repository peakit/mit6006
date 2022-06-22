"""
AVL Trees are augmented BST trees
which ensure that the trees are balanced
and hence height of the tree is log n.

All operations in BST were in O(h) where h
is the height of the tree. Now with balanced
BST trees those operations can run in O(log n)
"""


class Node:

    def __init__(self, key, parent, left, right, height=-1):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.height = height


class AVL:

    def __init__(self, root):
        self.root = root

    def insert(self, val):
        """
        Insert as in normal BST just that:
        - Keep incrementing height of every touched node
        - Rebalance tree from bottom to top seen nodes 
            of the tree
        """
        if self.root is None:
            newNode = Node(val, None, None, None)
            self.root = newNode
            return

        curr = self.root
        prev = None
        while curr is not None:
            is_left_child = False

            if val > curr.key:
                prev = curr
                curr.height = curr.height + 1
                curr = curr.right
                is_left_child = False
            elif val < curr.key:
                prev = curr
                curr.height = curr.height + 1
                curr = curr.left
                is_left_child = True

        newNode = Node(val, prev, None, None)
        if is_left_child:
            prev.left = newNode
        else:
            prev.right = newNode

        # TODO: recalculate balance factor for 
        # all touched nodes starting from left
        # to root
        self._rebalance(newNode)

    def search(self, val):
        """
        Search a given val in the AVL tree.
        Returns the node if found, None otherwise
        """
        curr = self.root
        while curr is not None:
            if val == curr.key:
                return curr
            elif val > curr.key:
                curr = curr.right
            else:
                curr = curr.left

        return curr

    def min(self, node=None):
        """
        Find minimum node in the given subtree.
        If the subtree node is not given then
        works from root
        """
        if node is None:
            node = self.root

        while node is not None and \
                node.left is not None:
            node = node.left
        return node

    def max(self, node=None):
        """
        Find minimum node in the given subtree.
        If the subtree node is not given then
        works from root
        """
        if node is None:
            node = self.root

        while node is not None and \
                node.right is not None:
            node = node.right
        return node

    def successor(self, node):
        """
        Returns the next larger node compared to given node.

        If there is right subtree then find_min(right_subtree)
        Else, keep following parent pointers till you find a 
        node which has left child or else successor is None
        """
        if node is None:
            return None

        if node.right is not None:
            return self.find_max(node.right)
        else:
            while node.parent is not None and \
                    node.parent.left != node:
                node = node.parent
            
            if node.parent.left == node:
                return node.parent

            return None
            

    def predecessor(self, node):
        """
        Returns the next smaller node compared to the given node.

        If left subtree exists then find_max(left_subtree).
        Else keep following parent pointers till you find a node
        which has right child or else predecessor is None
        """
        if node is None:
            return None
        
        if node.left is not None:
            return self.find_max(node.left)
        else:
            while node.parent is not None and \
                    node.parent.right != node:
                node = node.parent

            if node.parent.right == node:
                return node.parent

            return None

    def delete(self, node):
        """
        Delete node has 3 cases:
        1. node to be deleted has no children i.e. it is the
            leaf node. Just kill the node.
        2. node to be deleted has one child. Overwrite the 
            contents of the node with its children and also 
            set the parent and child pointers. And delete 
            the node
        3. node to be deleted has two children. Overwrite
            the contents of the node with its successor and
            call delete(succ)
        """

        if node is None:
            # the node to be deleted does not exist
            return
        
        if node.left is None and \
                node.right is None:
            # is a leaf node then just kill it
            if node == self.root:
                self.root = None
            elif node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
            
            parent = node.parent
            del node
            # TODO: recursively recalculate the height till 
            # root and rebalance the tree
        else:
            # node to be deleted has one child
            # just overwrite the contents of node
            # with the child which is there and
            # delete the node
            if node.left is None and \
                    node.right is not None:
                node.key = node.right.key
                node.right.parent = node.parent
                del node
            elif node.left is not None and \
                    node.right is None:
                node.key = node.left.key
                node.left.parent = node.parent
                del node
            else:
                # node to be deleted has two children
                # just overwrite the contents with 
                # the successor and call delete(succ)
                succ = self.successor(node)
                node.key = succ.key
                self.delete(succ)


    def _rebalance(self, node):
        pass


def capture_inputs():
    raw = input()
    return [int(r) for r in raw.split()]


def main():
    arr = capture_inputs()

    tree = AVL(None)
    for a in arr:
        tree.insert(a)


if __name__ == "__main__":
    main()
