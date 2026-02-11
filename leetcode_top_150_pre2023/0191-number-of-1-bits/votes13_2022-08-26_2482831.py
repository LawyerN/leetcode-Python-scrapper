def hammingWeight(self, n: int) -> int: # n = 00000000000000000000000000001011
        return bin(n).count("1")    # bin(n) = 0b1011