'''
Given two documents find the document distance between them. 
If two documents are similar then document distance will be 
less else document distance would be more.
'''
import math


def split_lines_to_words(document):
    words = document.split()
    return [w.lower() for w in words]


def count_word_freq(words):
    freq = {}
    for w in words:
        if freq.get(w) is None:
            freq[w] = 1
        else:
            freq[w] = freq[w] + 1
    return freq


def calculate_dot_product(freq1, freq2):
    prod = 0.0
    for w in freq1:
        if freq2.get(w) is not None:
            prod = prod + freq1[w] * freq2[w]
    return prod


def main():
    d1 = input()
    d2 = input()

    words1 = split_lines_to_words(d1)
    words2 = split_lines_to_words(d2)

    freq1 = count_word_freq(words1)
    freq2 = count_word_freq(words2)

    w1w2 = calculate_dot_product(freq1, freq2)
    w1w1 = calculate_dot_product(freq1, freq1)
    w2w2 = calculate_dot_product(freq2, freq2)

    p = math.acos(w1w2/(math.sqrt(w1w1 * w2w2)))
    print(p)


if __name__ == "__main__":
    main()
