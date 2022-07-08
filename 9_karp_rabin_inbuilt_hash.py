"""
Karp Rabin's rolling hash algorithm to do string matching

Relies on:
- using a sliding window
- calculating hash of each |s| width substring
- if the hash match then only match the string

This uses in-built hashing function to calculate the hash
"""


def search(t, s):
    indices = []
    for i in range(len(t) - len(s)):
        astring = t[i:i+len(s)]
        if hash(s) == hash(astring) and \
                s == astring:
            indices.append(i)
    return indices


def capture_inputs():
    print("Enter a long string=", end="")
    raw = input()
    t = raw
    print("Enter the substring to be searched=", end="")
    raw = input()
    s = raw

    return t, s


def main():
    t, s = capture_inputs()
    indices = search(t, s)
    print("=>The substring is present at following indices=", indices)


if __name__ == "__main__":
    main()
