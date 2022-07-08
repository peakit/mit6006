"""
Instead of using pre-built hash function for calculating
rolling hash in karp rabin algorithm, in this exercise
we will use a custom hash function.
"""


class RollingHash:
    """
    Needs to do in O(1)
    """

    def __init__(self, base_system, prime_number=31):
        self.store = list()
        self.base_system = base_system
        self.prime_number = prime_number
        self.hash_val = None

    def skip(self):
        """
        Skips the char
        """
        self.store = self.store[1:]

    def append(self, x):
        """
        Appends the given char x to the end of the current store
        """
        self.store.append(x)

    def calc_hash(self):
        """
        Calculates the hash of the current string store
        and store it
        """
        hvalue = 0
        for i in range(len(self.store)):
            part_value = ord(self.store[i])*pow(self.base_system, i)
            hvalue = hvalue + part_value
        self.hash_val = hvalue
        return self.hash_val

    def slide(self, old, new):
        """
        Given old character to drop and new character to add, this returns
        the updated hash value

        In base 'B' system:
            hash(abc) = a*B^0 + b*B^1 + c*B^2
        so Slide(a, d) would need to return 
            hash(bcd) = (hash(abc) - a*B^0)/B + d*B^2

        Further to avoid integer overflow in calculations, we use modulo with
        prime number
        """
        if old is None:
            self.append(new)
            return

        current_hash = self.hash_val
        if current_hash is None:
            current_hash = self.calc_hash()

        width = len(self.store)

        # calculate new hash with above calculations
        # ord() returns ascii value of unicode characters
        new_hash = (current_hash - ord(old))//self.base_system + \
            ord(new) * pow(self.base_system, width-1)

        # update the internal store
        self.skip()
        self.append(new)
        self.hash_val = new_hash


def search(s, t):
    """
    Searches for 's' in long string 't' and returns all the indices
    where it is found
    """
    found_idxs = []

    substring_rolling_hash = RollingHash(base_system=256)
    for ch in s:
        substring_rolling_hash.append(ch)
    substring_hash = substring_rolling_hash.calc_hash()

    main_string_rolling_hash = RollingHash(base_system=256)

    for i in range(0, len(t)):
            if i < len(s):
                old = None
            else:
                old = t[i - len(s)]

            main_string_rolling_hash.slide(old, t[i])
            rolling_hash = main_string_rolling_hash.hash_val
            if rolling_hash is not None and \
                    rolling_hash == substring_hash:
                if s == t[i - len(s) + 1:i + 1]:
                    found_idxs.append(i - len(s) + 1)

    return found_idxs


def capture_inputs():
    print("Enter long string=", end="")
    t = input()
    print("Enter substring to search=", end="")
    s = input()
    return t, s


def main():
    t, s = capture_inputs()
    found_idxs = search(s, t)
    print("The given substring was found at indices=", found_idxs)


if __name__ == "__main__":
    main()
