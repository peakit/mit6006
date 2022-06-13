'''
Insertion sort: Pairwise swaps
'''
def capture_inputs():
    raw_input = input()
    return [int(w) for w in raw_input.split()]


def main():
    elements = capture_inputs()
    n = len(elements)

    for i in range(1, n):
        for j in range(0, i):
            if elements[i] < elements[j]:
                temp = elements[i]
                elements[i] = elements[j]
                elements[j] = temp
    print(elements)


if __name__ == "__main__":
    main()
