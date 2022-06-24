"""
AVL Trees are augmented BST trees
which ensure that the trees are balanced
and hence height of the tree is log n.

All operations in BST were in O(h) where h
is the height of the tree. Now with balanced
BST trees those operations can run in O(log n)
"""
import math


class Node:

    def __init__(self, key, parent, left, right, height=0):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.height = height


class AVL:

    def __init__(self, root):
        self.root = root

    def recalculate_height(self, subtree):
        """
        Recalculate height of all nodes under this subtree (inclusive)
        and updates it. Generally, this would be called with the root 
        node so that the entire tree's height is updated

        height = 1 + max(left.height, right.height)
        """
        if subtree is None:
            return -1

        height_left = self.recalculate_height(subtree.left)
        height_right = self.recalculate_height(subtree.right)

        height = 1 + max(height_left, height_right)

        # update height
        subtree.height = height
        return height

    def balance_factor(self, node):
        """
        Calculates balance factor and returns it

        BF = height of left child - height of right child
        """
        h_left = -1
        h_right = -1

        if node.left is not None:
            h_left = node.left.height
        if node.right is not None:
            h_right = node.right.height

        return h_left - h_right

    def is_balanced(self, node):
        """
        If BF > 1 or BF < -1 that means subtree is unbalanced
        else keep recursing upwards

        Returns the bf_status and unbalanced_node that is first
        encountered in the ancestoral path
        """
        if node is None:
            return True, None

        bf = self.balance_factor(node)
        if bf > 1 or bf < -1:
            return False, node

        # recurse in the upwards direction of the tree
        return self.is_balanced(node.parent)

    def rotate(self, node):
        """
        Figures out the current orientation of the subtree
        and applies one or more orientations to balance
        the tree
        1. LL => rotate_right
        2. RR => rotate_left
        3. RL => rotate_right(node.right) followed by rotate_left(node)
        4. LR => rotate_left(node.left) followed by rotate_right(node)
        """
        orn = self.find_orientation(node)
        if orn == "RR":
            print("Rotate-Left ", node.key)
            self.rotate_left(node)
        elif orn == "LL":
            print("Rotate-Right ", node.key)
            self.rotate_right(node)
        elif orn == "RL":
            # case of wedge
            # rotate the "right child" to left to bring linear
            # orientation of RR
            print("Rotate-Right ", node.right.key,
                  " and then Rotate-Left ", node.key)
            self.rotate_right(node.right)
            # followed by normal left rotation of node
            self.rotate_left(node)
        else:
            # LR - similar to above wedge case
            print("Rotate-Left ", node.left.key,
                  " and then Rotate-Right ", node.key)
            self.rotate_left(node.left)
            self.rotate_right(node)

    def find_orientation(self, node):
        """
        Finds which of the orientation does the unbalanced subtree
        lies:
        1. LL
        2. RR
        3. RL
        4. LR

        Returns the orientation string
        """
        bf = self.balance_factor(node)
        orientation = []
        if bf < -1:
            # right subtree is more heavy
            orientation.append("R")
            bf_rchild = self.balance_factor(node.right)
            if bf_rchild < 0:
                orientation.append("R")
            else:
                orientation.append("L")
        else:
            # left subtree is more heavy
            orientation.append("L")
            bf_lchild = self.balance_factor(node.left)
            if bf_lchild < 0:
                orientation.append("R")
            else:
                orientation.append("L")

        return "".join(orientation)

    def rotate_left(self, node):
        """
        Rotate left from the given node

        Overall steps:
        1. Backup the current node's parent
        2. Point to new root
        3. Handle pointer of "shifting node" R->L, if any
        4. Hang the (old root) node as left child of new root
        5. Handle pointer to the new root's parent depending upon
            left child of parent, right child or root of the tree
        """
        # step 1: Backup parent of the node
        parent = node.parent

        # step 2: Point to new root
        newRoot = node.right

        # step 3: Handle the ptrs of R->L
        # "shifting node", if any
        if node.right.left is not None:
            node.right = node.right.left
            node.right.parent = node
        else:
            # else, now the node won't have right
            # child, let's clear the ptr
            node.right = None

        # step 4: Make the old node as
        # left child of new root
        newRoot.left = node
        node.parent = newRoot

        newRoot.parent = parent

        if parent is not None and \
                parent.left == node:
            # step 5: if the node to be
            # rotated is left child of its
            # parent
            parent.left = newRoot
        elif parent is not None and \
                parent.right == node:
            # step 5: if the node to be rotated
            # is right child of its parent
            parent.right = newRoot
        else:
            # step 5: node's parent does not exist
            # that is, the current root is being
            # rotated
            self.root = newRoot

    def rotate_right(self, node):
        """
        Rotate right from the given node

        Overall steps:
        1. Backup the node's parent
        2. Point to newRoot
        3. Handle pointers of any "shifting node" L->R
        4. Hang the (old root) node as right child of newRoot
        5. Handle pointer to the newRoot's parent depending
            upon left child, right child of parent or root node
        """

        # step 1. Backup the node's parent
        parent = node.parent

        # step 2. Point to newRoot
        newRoot = node.left

        # step 3: Handle pointers of any "shifting node" L->R
        if newRoot.right is not None:
            node.right.left = newRoot.right
            newRoot.right.parent = newRoot
        else:
            # else, now the node won't have
            # left child, let's clear the ptr
            node.left = None

        # step 4. Hang the (old root) node as right child of newRoot
        newRoot.right = node
        node.parent = newRoot

        newRoot.parent = parent
        if parent is not None and \
                parent.left == node:
            # step 5: If node was left child of its parent
            parent.left = newRoot
        elif parent is not None and \
                parent.right == node:
            # step 5: If node was right child of its parent
            parent.right = newRoot
        else:
            # step 5: If the node is the root node of the tree
            self.root = newRoot

    def insert(self, val):
        """
        Insert as in normal BST just that:
        - Keep incrementing height of every touched node
        - Rebalance tree from bottom to top seen nodes 
            of the tree
        """
        print("Inserting ", val, " in the AVL tree..")
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
                # curr.height = curr.height + 1
                curr = curr.right
                is_left_child = False
            elif val < curr.key:
                prev = curr
                # curr.height = curr.height + 1
                curr = curr.left
                is_left_child = True

        newNode = Node(val, prev, None, None)
        if is_left_child:
            prev.left = newNode
        else:
            prev.right = newNode

        # recalculate height of the entire tree
        self.recalculate_height(self.root)

        # check if AVL is balanced (upto the root)
        bal_status, unbalanced_node = self.is_balanced(newNode)
        if not bal_status:
            # do one or more rotations
            self.rotate(unbalanced_node)
            # recalculate the height
            self.recalculate_height(self.root)

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

        parent = node.parent
        if node.left is None and \
                node.right is None:
            # is a leaf node then just kill it
            if node == self.root:
                self.root = None
            elif node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None

            del node
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
        # recalculate the height of the tree starting
        # from its root
        self.recalculate_height(self.root)
        bal_status, unbal_node = self.is_balanced(parent)
        if not bal_status:
            self.rotate(unbal_node)
        self.recalculate_height(self.root)

    @staticmethod
    def _rec_inorder_traversal(node):
        """
        Recursively prints the inorder traversal of the tree
        """
        if node is None:
            return

        AVL._rec_inorder_traversal(node.left)
        print(node.key, end=" ")
        AVL._rec_inorder_traversal(node.right)

    def inorder_traversal(self):
        """
        Prints inorder traversal of the tree
        """
        AVL._rec_inorder_traversal(self.root)


def capture_inputs():
    raw = input()
    return [int(r) for r in raw.split()]


def main():
    arr = capture_inputs()

    tree = AVL(None)
    for a in arr:
        tree.insert(a)
    tree.inorder_traversal()


if __name__ == "__main__":
    main()
