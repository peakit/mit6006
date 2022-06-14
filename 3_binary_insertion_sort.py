'''
Improvised insertion sort which finds the right position where to
insert an element in a sorted array by using Binary search.
Time complexity comes down from O(n^2) to O(n logn)
'''


def capture_inputs():
    raw_input = input()
    return [int(w) for w in raw_input.split()]


def binary_search(start, end, arr, ele):
    '''
    Searches the position of given ele in arr's start to end index
    '''
    if start == end:
        if ele > arr[start]:
            return start + 1
        else:
            return start
    
    if start > end:
        return start

    mid = start + (end - start)//2
    if ele < arr[mid]:
        end = mid - 1
        return binary_search(start, end, arr, ele)
    elif ele > arr[mid]:
        start = mid + 1
        return binary_search(start, end, arr, ele)
    else:
        return mid


def main():
    elements = capture_inputs()
    n = len(elements)

    for i in range(1, n):
        ele = elements[i]
        idx = binary_search(0, i - 1, elements, ele)
        elements = elements[:idx] + [ele] + elements[idx:i] + elements[i+1:]

    print(elements)


if __name__ == "__main__":
    main()
