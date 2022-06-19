"""
- Assume airport with single runway
- Obviously single runway would be busy
- Reservations for future landings
- Reserve request specified landing time `t`
- Add `t` to the set `R` if no other landings are scheduled within `k` minutes
- Remove from set `R` after plane lands

Do runway reservations in O(log n) time complexity
"""


class Node:

    def __init__(self, key, parent, left, right):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class Tree:

    def __init__(self, root):
        self.root = root

    def insert(self, t, k):
        """
        Insert node t with k spacing
        """
        if self.root is None:
            self.root = Node(t, None, None, None)
            return True, None

        curr = self.root
        prev = None
        while curr is not None:
            if t < curr.key:
                prev = curr
                curr = curr.left
            elif t > curr.key:
                prev = curr
                curr = curr.right

        if t >= prev.key + k:
            newNode = Node(t, prev, None, None)
            prev.right = newNode
            return True, None
        elif t <= prev.key - k:
            newNode = Node(t, prev, None, None)
            prev.left = newNode
            return True, None
        else:
            return False, "=>Not able to ensure spacing of " + str(k)

    def find_min(self, subtree=None):
        """
        Find min in the subtree which is given else start from root
        """
        if subtree is None:
            curr = self.root
        else:
            curr = subtree

        if curr is None:
            return

        while curr.left is not None:
            curr = curr.left
        return curr

    def successor(self, node):
        """
        Give next larger node compared to
        given node's key
        """
        if node.right is not None:
            return self.find_min(node.right)
        
        curr = node
        while curr.parent is not None \
            and curr.parent.left == curr:
            curr = curr.parent
        return curr


    def delete(self, node):
        if node is None:
            return False, "=>No plane in queue to land"
        elif node.left is None \
                and node.right is None:
            if node.parent is not None \
                    and node.parent.left == node:
                node.parent.left = None
                del node
            elif node.parent is not None \
                    and node.parent.right == node:
                node.parent.right = None
                del node
            else:
                del node
                self.root = None
        else:
            succ = self.successor(node)
            node.key = succ.key
            if succ.parent.left == succ:
                succ.parent.left = succ.left
                succ.left.parent = succ.parent
            elif succ.parent.right == succ:
                succ.parent.right = succ.right
                succ.right.parent = succ.parent
            del succ
        return True, None
    
    @staticmethod
    def _rec_inorder_traversal(node):
        if node is None:
            return
        Tree._rec_inorder_traversal(node.left)
        print(node.key, end=" ")
        Tree._rec_inorder_traversal(node.right)

    def inorder_traversal(self, node=None):
        if node is None:
            Tree._rec_inorder_traversal(self.root)
        else:
            Tree._rec_inorder_traversal(node)

tree = Tree(None)


def show_menu():
    print("\nPress 1 to make reservation")
    print("Press 2 to land")
    print("Press 3 to show current reservations")
    print("Press 4 to exit the system")


def capture_choice():
    print("\nPlease enter your choice here=", end="")
    c = input()
    return int(c)


def make_reservation(k):
    print("Enter the time at which runway reservation is needed=", end="")
    t = int(input())

    status, msg = tree.insert(t, k)
    if not status:
        print(msg)


def make_landing():
    minn = tree.find_min()
    status, msg = tree.delete(minn)
    if not status:
        print(msg)

def show_reservations():
    tree.inorder_traversal()

def main():
    exit_system = False
    print("\nEnter the minimum spacing to ensure between landings=", end="")
    k = int(input())

    while not exit_system:
        show_menu()
        choice = capture_choice()
        if choice == 1:
            make_reservation(k)
        elif choice == 2:
            make_landing()
        elif choice == 3:
            show_reservations()
        elif choice == 4:
            exit_system = True
        else:
            print("=>Wrong choice!")


if __name__ == "__main__":
    main()
