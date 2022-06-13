'''
Finds peak element in a 2D array
'''


def capture_inputs(matrix):
    print("Enter num of rows: ")
    rows = int(input())
    print("Enter elements of each row")
    for i in range(rows):
        raw_rows = input()
        elements = [int(r) for r in raw_rows.split()]
        matrix.append(elements)


def find_max_idx(matrix):
    num_rows = len(matrix) - 1
    num_cols = len(matrix[0])
    maxx = 0.0
    maxx_row = 0
    for i in range(num_rows):
        if matrix[i][0] > maxx:
            maxx = matrix[i][0]
            maxx_row = i
    return maxx_row, 0


def find_peak(start, end, elements):
    # 1D peak finding code copied

    sz = len(elements)
    # Case 1: only one element in the array
    if sz == 1:
        return elements[0]

    # Case 2: first element is the peak
    if elements[0] >= elements[1]:
        return elements[0]
    # Case 3: last element is the peak
    if elements[sz - 1] >= elements[sz - 2]:
        return elements[sz - 1]

    mid = int((end + start)/2)

    if elements[mid] >= elements[mid - 1] and elements[mid] >= elements[mid + 1]:
        return elements[mid]

    if elements[mid - 1] >= elements[mid]:
        return find_peak(0, mid-1, elements)
    if elements[mid + 1] >= elements[mid]:
        return find_peak(mid + 1, end, elements)


def main():
    matrix = list()
    capture_inputs(matrix)

    # Step1: Find maximum in one of the columns
    row, col = find_max_idx(matrix)

    # Step2: Locate peak in row where global maxima was found
    peak = find_peak(0, len(matrix[row]) - 1, matrix[row])
    print("peak=", peak)


if __name__ == '__main__':
    main()
