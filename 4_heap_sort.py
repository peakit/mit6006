"""
Heap sort: 
1. Build a heap out of given elements by iteratively
moving largest to parent node
2. Keep extracting maximum i.e. root node and 
re-heapfiying the tree starting from its root node
"""


def max_heapify(arr, i):
    """
    Bottom-up keep moving the largest of the sibling to Root of the sub-tree.
    This needs to be done starting from first non-leaf node downto root
    node of the tree.
    O(logn)
    """
    # max_heapify is deemed complete if i > both its children
    # swap with largest of the children
    left_exists = False
    right_exists = False
    if (2*i + 1) < len(arr):
        left_exists = True
    if (2*i + 2) < len(arr):
        right_exists = True

    left_is_largest = False
    right_is_largest = False

    if left_exists and right_exists:
        if arr[2*i + 1] > arr[2*i + 2]:
            left_is_largest = True
        else:
            right_is_largest = True
    elif left_exists and not right_exists:
        if arr[2*i + 1] > arr[i]:
            left_is_largest = True
    elif right_exists and not left_exists:
        if arr[2*i + 2] > arr[i]:
            right_is_largest = True
    else:
        # neither left nor right is largest (i.e. none of these two exists)
        # and hence root is already largest
        left_is_largest = False
        right_is_largest = False

    if left_is_largest and arr[2*i + 1] > arr[i]:
        temp = arr[2*i + 1]
        arr[2*i + 1] = arr[i]
        arr[i] = temp
        max_heapify(arr, 2*i + 1)
    elif right_is_largest and arr[2*i + 2] > arr[i]:
        temp = arr[2*i + 2]
        arr[2*i + 2] = arr[i]
        arr[i] = temp
        max_heapify(arr, 2*i + 2)


def build_heap(arr):
    """
    O(n logn)
    """
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        max_heapify(arr, i)


def capture_inputs():
    raw_input = input()
    return [int(w) for w in raw_input.split()]


def heap_sort(arr):
    """
    Root has the largest element in a max-heap so
    you swap root with last element of the array
    and return the last element and then max-heapify
    the new root and shrink the array by 1
    """
    # swap root with last element
    largest = arr[0]
    arr[0] = arr[len(arr) - 1]
    arr[len(arr) - 1] = largest
    arr = arr[:len(arr)-1]   # shrinking array by 1

    max_heapify(arr, 0)
    return largest, arr  # we also return the newly shrunked array!


def main():
    arr = capture_inputs()

    # Step 1: Build heap and internally max-heapifying it
    build_heap(arr)
    print("After max-heapify, the heap looks like: ", arr)

    # Step 2: Perform heap sort
    for i in range(0, len(arr)):
        largest, arr = heap_sort(arr)
        print(largest)


if __name__ == "__main__":
    main()
