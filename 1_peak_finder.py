"""
Finding peak in a 1D array. A peak is 
an element in the array such that element
on the left and right of it is smaller
i.e. a[i] > a[i-1] and a[i] > a[i+1]
"""


def find_peak(start, end, elements):
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
    raw_input = input()
    elements = [int(e) for e in raw_input.split()]

    peak = find_peak(0, len(elements), elements)
    print("peak=",peak)


if __name__ == "__main__":
    main()
