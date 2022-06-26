"""
Counting sort is a Linear sorting algorithm which 
1. Does not use Comparisons
2. Used when the element value is capped in an array, each element
    is non-negative integer
3. If n is the size of array then only k unique values in array (k < n)
4. Does stable sorting i.e. the original order of an element which is duplicated
    remains same in the output sorted array
5. Time complexity O(n+k) and requires auxiliary space O(n+k)
"""


def counting_sort(arr):

    # step 1: Find the range of unique values
    maxx = max(arr)
    minn = min(arr)

    # step 2: record occurrences in counted list
    k = maxx - minn + 1
    counted = [0 for e in range(k)]
    for a in arr:
        counted[a - minn] = counted[a - minn] + 1

    # step 3: Starting from reverse sum the element &
    # the previous element
    for i in range(1, len(counted)):
        counted[i] = counted[i] + counted[i - 1]

    # step 4: Shift right this accumulated array and
    # backfill by 0
    for i in reversed(range(len(counted))):
        if i == 0:
            counted[i] = 0
        else:
            counted[i] = counted[i - 1]

    # step 5: Go over the original array and keep
    # looking for its right index in the above counted
    # array. Increment the existing index value so that
    # next duplicate occurrence finds the next slot
    output = [None]*len(arr)
    for a in arr:
        idx = counted[a - minn]
        output[idx] = a
        counted[a - minn] = idx + 1

    return output


def capture_inputs():
    raw_input = input()
    return [int(r) for r in raw_input.split()]


def main():
    arr = capture_inputs()
    sorted_arr = counting_sort(arr)
    print("Sorted array:", sorted_arr)


if __name__ == "__main__":
    main()
