"""
Radix sort

- Uses Counting sort internally
- Sort elements by number at first once place, 
    then hundredth and so on
- Assuming numbers are in base 10 system
- Completes sorting in O(w(n+k)) where 
    w is max number of letters in a number
    n is total number of elements
    k is the actual unique elements in each 
        iteration of counting sort
"""


def radix_sort(arr):
    maxx = max(arr)
    num_radices = len(str(maxx))
    for r in range(num_radices):
        arr = counting_sort(arr, r, num_radices)
    return arr


def counting_sort(arr, target_radix, num_radices):
    # step 1: count the occurrences
    counted = [0]*10  # since base 10 system
    for a in arr:
        # gets the once, tens, hundredth and so on number for each array element,
        # else gets zero
        a_idx = int((str(a).zfill(num_radices))[num_radices - target_radix - 1])
        counted[a_idx] = counted[a_idx] + 1

    # step 2: accumulate the occurrences, a[i] = a[i] + a[i-1]
    for i in range(1, len(counted)):
        counted[i] = counted[i] + counted[i - 1]

    # step 3: shift right, backfill by 0
    for i in reversed(range(len(counted))):
        if i == 0:
            counted[i] = 0
        else:
            counted[i] = counted[i-1]

    output = [None] * len(arr)
    for a in arr:
        # gets the once, tens, hundredth and so on number for each array element
        a_idx = int((str(a).zfill(num_radices))[num_radices - target_radix - 1])
        output[counted[a_idx]] = a
        counted[a_idx] = counted[a_idx] + 1
    return output


def capture_inputs():
    raw_input = input()
    return [int(r) for r in raw_input.split()]


def main():
    arr = capture_inputs()
    output = radix_sort(arr)
    print("Sorted array: ", output)


if __name__ == "__main__":
    main()
