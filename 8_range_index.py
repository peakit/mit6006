"""
Support a special kind of range index, to speed up the operations.

1. The range index must support fast (sub-linear) insertions
2. The range index must also be able to compute the minimum and 
    maximum over all keys quickly (in sub-linear time).
"""


class Node:

    def __init__(self, key, left, right, parent):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent


class BST:

    def __init__(self, root):
        self.root = root

    def insert(self, val):
        """
        Inserts a given val in the BST tree
        """
        new_node = Node(val, None, None, None)
        insertion_point = self.find_insertion_point(val)

        if insertion_point is None:
            # insert as root
            self.root = new_node
        else:
            if val < insertion_point.key:
                insertion_point.left = new_node
            else:
                insertion_point.right = new_node

        new_node.parent = insertion_point

    def find_insertion_point(self, val):
        """
        Returns the parent node whose child will this val node become.
        If the val node would make it as root of the tree then None 
        is returned.
        """
        prev = None
        curr = self.root
        while curr is not None:
            if val > curr.key:
                prev = curr
                curr = curr.right
            elif val < curr.key:
                prev = curr
                curr = curr.left
            else:
                # current key is equal to val
                break

        return prev

    def range_search(self, lo, hi):
        """
        Performs a range search and returns list of
        values which are between closed set [lo, hi]
        """
        curr = self.root
        answers = list()

        # step 1: simulate an insertion of lo and hi
        #           and find the insertion points
        lo_insertion_pt = self.find_insertion_point(lo)
        hi_insertion_pt = self.find_insertion_point(hi)

        if lo_insertion_pt is not None and \
                hi_insertion_pt is not None:
            # step 2: Find lowest common ancestor for lo and hi
            #           insertion pts.
            lca = self.find_lowest_common_ancestor(lo_insertion_pt,
                                                   hi_insertion_pt)

            # step 3: Perform an inorder traversal of the LAC
            #           while doing the range check on the keys
            answers = self.inorder_traversal(lca, lo, hi)

        return answers

    def find_lowest_common_ancestor(self, lo_insertion_pt,
                                    hi_insertion_pt):
        """
        Finds lowest common ancestor

        Start from root keep going in the direction where both lo and hi exist.
        If we reach a point in the tree where lo and hi are not on one side of 
        the subtree then we break.
        """
        curr = self.root
        while curr is not None:
            if lo_insertion_pt.key < curr.key and \
                    hi_insertion_pt.key < curr.key:
                curr = curr.left
            elif lo_insertion_pt.key > curr.key and \
                    hi_insertion_pt.key > curr.key:
                curr = curr.right
            else:
                break
        return curr

    def inorder_traversal(self, subtree, lo, hi):
        """
        Performs inorder traversal by limiting keys to be between
        lo and hi (inclusive)
        """
        result = list()
        BST._rec_inorder_traversal(subtree, lo, hi, result)
        return result

    @staticmethod
    def _rec_inorder_traversal(subtree, lo, hi, result):
        if subtree is None:
            return

        BST._rec_inorder_traversal(subtree.left, lo, hi, result)
        if subtree.key >= lo and \
                subtree.key <= hi:
            result.append(subtree.key)
        BST._rec_inorder_traversal(subtree.right, lo, hi, result)


def capture_inputs():
    print("Enter elements to be inserted in BST tree=", end="")
    raw = input()
    arr = [int(r) for r in raw.split()]
    print("Enter range (lo hi) within which to perform search=", end="")
    raw = input()
    lohi = [int(r) for r in raw.split()]
    return arr, lohi[0], lohi[1]


def main():
    arr, lo, hi = capture_inputs()
    bst = BST(None)
    for a in arr:
        bst.insert(a)

    print(bst.range_search(lo, hi))


if __name__ == "__main__":
    main()
