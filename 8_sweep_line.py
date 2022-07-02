"""
Sweep line algorithm

This algorithm is used to find the intersection point between
two lines. Without this algorithm we would need to process
two lines at a time to check for their intersection. That is,
total nc2 combinations. And that means, time complexity of n^2

E.g. problems
1. Given birth and death date of people, find the population
    as of given year
2. Given the coordinates of many skyscrappers, find the 
    contour of the skyline formed by these skyscrappers
3. Given the day ranges when flowers bloom, find the how 
    many blooming flowers you will notice on a specific
    date

PS: Does not handle the case when one of the lines is a vertical
    line
"""

from abc import ABC, abstractmethod
from enum import Enum


class Side(Enum):
    LEFT = 1
    RIGHT = 2


class Node(ABC):

    left = None
    right = None
    parent = None
    height = 0

    @abstractmethod
    def get_key(self):
        pass


class Coord(Node):

    def __init__(self, x, y, side=None, otherCoord=None):
        self.x = x
        self.y = y
        self.side = side
        self.otherCoord = otherCoord

    def assignSideTags(self):
        """
        Assign side tags on self and self.otherCoord
        """
        if self.otherCoord is None:
            raise Exception(
                "Other coord is not set on this coordinate.",
                "Unable to assign side tags!")

        if self.x < self.otherCoord.x:
            self.side = Side.LEFT
            self.otherCoord.side = Side.RIGHT
        else:
            self.side = Side.RIGHT
            self.otherCoord.side = Side.LEFT

    def check_intersection(self, coord_other):

        if coord_other is None:
            return False

        line1_slope = (self.otherCoord.y - self.y)/(self.otherCoord.x - self.x)
        line2_slope = (coord_other.otherCoord.y - coord_other.y) / \
            (coord_other.otherCoord.x - coord_other.x)

        # line equation => y - y1 = m(x - x1) or
        #                  y = m(x - x1) + y1
        # line1_equation = line1_slope(x - self.x) + self.y
        # line2_equation = line2_slope(x - coord_other.x) + coord_other.y

        # intersection_pt_x => line1_slope*x - line2_slope*x = coord_other.y - self.y + line2_slope*coord_other.x + line1_slope*self.x
        intersection_pt_x = (coord_other.y - self.y + line2_slope *
                             coord_other.x + line1_slope*self.x)/(line1_slope - line2_slope)

        # Put above value of x in any one of the equations
        # to find intersection pt y
        intersection_pt_y = line1_slope(intersection_pt_x - self.x) + self.y

        # intersection pt should lie between the line segments
        xmin = min(self.x, self.otherCoord.x)
        xmax = max(self.x, self.otherCoord.x)
        ymin = min(self.y, self.otherCoord.y)
        ymax = max(self.y, self.otherCoord.y)

        xmin_coord_other = min(coord_other.x, coord_other.otherCoord.x)
        xmax_coord_other = max(coord_other.x, coord_other.otherCoord.x)
        ymin_coord_other = min(coord_other.y, coord_other.otherCoord.y)
        ymax_coord_other = max(coord_other.y, coord_other.otherCoord.y)

        if intersection_pt_x >= xmin and \
                intersection_pt_x <= xmax and \
                intersection_pt_y >= ymin and \
                intersection_pt_y <= ymax and \
                intersection_pt_x >= xmin_coord_other and \
                intersection_pt_x <= xmax_coord_other and \
                intersection_pt_y >= ymin_coord_other and \
                intersection_pt_y <= ymax_coord_other:
            return True, tuple(intersection_pt_x, intersection_pt_y)
        else:
            return False, None

    def get_key(self):
        return self.y


class AVL:

    def __init__(self, root):
        self.root = root

    def recalculate_height(self, subtree):
        """
        Bottom up re-calculation of height
        """
        if subtree is None:
            return -1

        h_l = self.recalculate_height(subtree.left)
        h_r = self.recalculate_height(subtree.right)

        height = max(h_l, h_r) + 1
        subtree.height = height
        return height

    def balance_factor(self, node):
        h_l = -1
        h_r = -1
        if node.left is not None:
            h_l = node.left.height
        if node.right is not None:
            h_r = node.right.height

        return h_l - h_r

    def is_balanced(self, node):
        """
        Bottom up check to determine if AVL is 
        balanced or not
        """
        if node is None:
            return True, None

        balance_factor = self.balance_factor(node)
        if balance_factor < -1 or \
                balance_factor > 1:
            return False, node

        return self.is_balanced(node.parent)

    def check_orientation(self, unbal_node):
        bf = self.balance_factor(unbal_node)
        orientation = []
        if bf < -1:
            orientation.append('R')
            bf_r = self.balance_factor(unbal_node.right)
            if bf_r <= -1:
                orientation.append('R')
            else:
                orientation.append('L')
        else:
            orientation.append('L')
            bf_l = self.balance_factor(unbal_node.left)
            if bf_l <= -1:
                orientation.append('R')
            else:
                orientation.append('L')

        return ''.join(orientation)

    def rotate(self, unbal_node):
        orientation = self.check_orientation(unbal_node)
        if orientation == 'LL':
            self.rotate_right(unbal_node)
        elif orientation == 'RR':
            self.rotate_left(unbal_node)
        elif orientation == 'LR':
            self.rotate_left(unbal_node.left)
            self.rotate_right(unbal_node)
        else:
            self.rotate_right(unbal_node.right)
            self.rotate_left(unbal_node)

    def rotate_left(self, node):
        parent = node.parent
        new_root = node.right
        new_root.parent = parent

        if new_root.left is not None:
            node.right = new_root.left
            node.right.parent = node
        else:
            node.right = None

        node.parent = new_root
        new_root.left = node

        if parent is not None and \
                parent.left == node:
            parent.left = new_root
        elif parent is not None and \
                parent.right == node:
            parent.right = new_root
        else:
            self.root = new_root

    def rotate_right(self, node):
        parent = node.parent
        new_root = node.left
        new_root.parent = parent

        if new_root.right is not None:
            node.left = new_root.right
            node.left.parent = node
        else:
            node.left = None

        node.parent = new_root
        new_root.right = node

        if parent is not None and \
                parent.left == node:
            parent.left = new_root
        elif parent is not None and \
                parent.right == node:
            parent.right = new_root
        else:
            self.root = new_root

    def insert(self, subtree, new_node):
        """
        Inserts given new node in the given subtree
        """
        if subtree is not None and \
                new_node.get_key() > subtree.get_key():
            if subtree.right is None:
                subtree.right = new_node
                new_node.parent = subtree
                self.recalculate_height(self.root)
                balanced, unbal_node = self.is_balanced(subtree)
                if not balanced:
                    self.rotate(unbal_node)
                    self.recalculate_height(self.root)
            else:
                self.insert(subtree.right, new_node)
        elif subtree is not None and \
                new_node.get_key() < subtree.get_key():
            if subtree.left is None:
                subtree.left = new_node
                new_node.parent = subtree
                self.recalculate_height(self.root)
                balanced, unbal_node = self.is_balanced(subtree)
                if not balanced:
                    self.rotate(unbal_node)
                    self.recalculate_height(self.root)
            else:
                self.insert(subtree.left, new_node)
        else:
            # probably, inserting new root
            self.root = new_node

    def delete(self, del_node):
        """
        Deletes given node from AVL tree
        """
        parent = del_node.parent
        if del_node.left is None and \
                del_node.right is None:
            if del_node == self.root:
                self.root = None
            elif parent.left == del_node:
                parent.left = None
            else:
                parent.right = None
            del del_node
        elif del_node.left is None and \
                del_node.right is not None:
            if del_node == self.root:
                self.root = None
            elif parent.left == del_node:
                parent.left = del_node.right
            else:
                parent.right = del_node.right
            del_node.right.parent = parent
            del del_node
        elif del_node.left is not None and \
                del_node.right is None:
            if del_node == self.root:
                self.root = None
            elif parent.left == del_node:
                parent.left = del_node.left
            else:
                parent.right = del_node.left
            del_node.left.parent = parent
            del del_node
        else:
            # both child of del node exists
            succ = self.successor(del_node)
            # copy contents
            del_node.x = succ.x
            del_node.y = succ.y
            del_node.otherCoord.x = succ.otherCoord.x
            del_node.otherCoord.y = succ.otherCoord.y
            # succ may have right subtree
            # but never left subtree
            self.delete(succ)

        self.recalculate_height(self.root)
        balanced, unbal_node = self.is_balanced(parent)
        if not balanced:
            self.rotate(unbal_node)
            self.recalculate_height(self.root)

    def min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def successor(self, node):
        if node.right is not None:
            return self.min(node.right)
        else:
            curr = node
            while curr.parent is not None and \
                    curr.parent.left != curr:
                curr = curr.parent

            if curr.parent is None:
                return None
            else:
                return curr.parent

    def predecessor(self, node):
        if node.left is not None:
            return self.max(node.left)
        else:
            curr = node
            while curr.parent is not None and \
                    curr.parent.right != curr:
                curr = curr.parent

            if curr.parent is None:
                return None
            else:
                return curr.parent


def capture_inputs():
    print("Enter number of lines=", end="")
    num_lines = int(input())

    all_coords = list()
    for l in range(num_lines):
        print("\nEnter x1 and y1 coordinates (x,y)=", end="")
        raw = input()
        coord = [int(r) for r in raw.split(",")]
        c1 = Coord(coord[0], coord[1])

        print("Enter x2 and y2 coordinates (x,y)=", end="")
        raw = input()
        coord = [int(r) for r in raw.split(",")]
        c2 = Coord(coord[0], coord[1])

        c1.otherCoord = c2
        c2.otherCoord = c1

        c1.assignSideTags()
        all_coords.append(c1)
        all_coords.append(c2)

    return all_coords


def main():
    all_coords = capture_inputs()

    # step 1: Sort the lines using their x coordinates
    # and tag with "left" and "right" ends
    all_coords_sorted = sorted(all_coords, key=lambda c: c.x)

    # step 2: Move from leftmost x coordinate to next
    # higher x coordinate

    # step 3: Do "vertical sweep":
    # 1. If it is left endpoint then check intersection
    #   with just upper and lower line segments
    # 2. If it is right endpoint then check intersection
    #   of just upper and lower line segments since this
    #   line is now out of active set itself
    tree = AVL(None)
    intersection_count = 0
    intersections = list()
    for coord in all_coords_sorted:
        if coord.side == Side.LEFT:
            tree.insert(tree.root, coord)
            succ = tree.successor(coord)
            pred = tree.predecessor(coord)
            if succ is not None:
                is_intersecting, intersection_pt = coord.check_intersection(succ)
                if is_intersecting:
                    # count as an intersection
                    intersection_count = intersection_count + 1
                    intersections.append(intersection_pt)

            if pred is not None:
                is_intersecting, intersection_pt = coord.check_intersection(pred)
                if is_intersecting:
                    # count as an intersection
                    intersection_count = intersection_count + 1
                    intersections.append(intersection_pt)
        else:
            # delete the coordinate pair representing
            # this line segment
            # the right coordinate is never inserted in the tree
            # only the LEFT pair was inserted and deleted now
            tree.delete(coord.otherCoord)

            succ = tree.successor(coord)
            pred = tree.predecessor(coord)
            if succ is None or pred is None:
                continue

            is_intersecting, intersection_pt = succ.check_intersection(pred)
            if is_intersecting:
                # count as an intersection
                intersection_count = intersection_count + 1
                intersections.append(intersection_pt)

    print("Total Intersections=", intersection_count)
    print("Intersections=", intersections)


if __name__ == "__main__":
    main()
