'''
Merge sort -O (n logn)
'''


def merge(m1, m2):
    '''
    Merges two sorted lists
    '''
    i = 0
    j = 0
    output = []
    while(i < len(m1) and j < len(m2)):
        if m1[i] > m2[j]:
            output.append(m2[j])
            j = j + 1
        else:
            output.append(m1[i])
            i = i + 1

    if i < len(m1):
        output.extend(m1[i:])
    if j < len(m2):
        output.extend(m2[j:])

    return output


def merge_sort(start, end, arr):
    if start >= end:
        return [arr[start]]

    mid = start + (end - start)//2

    m1 = merge_sort(start, mid, arr)
    m2 = merge_sort(mid+1, end, arr)

    return merge(m1, m2)


def capture_input():
    raw_input = input()
    return [int(w) for w in raw_input.split()]


def main():
    arr = capture_input()
    output = merge_sort(0, len(arr) - 1, arr)
    print(output)


if __name__ == "__main__":
    main()
