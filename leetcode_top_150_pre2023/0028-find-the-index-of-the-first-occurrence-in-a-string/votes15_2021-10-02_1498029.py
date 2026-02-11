import functools
import random


class Solution(object):
    
    # Pick a random hash function from a universal family with a small collision probability |pattern| / p.
    p = 1000000007
    x = random.randint(1, p - 1)
    
    def strStr(self, haystack, needle):
        
        # Empty pattern edge case.
        if needle == "":
            return 0
        
        # Find all occurances of pattern and return 1st (extended to "find all" by dropping [0]).
        positions = self.rabin_karp(pattern=needle, text=haystack)
        return -1 if not positions else positions[0]
    
    @classmethod
    def rabin_karp(cls, pattern, text):
        """Find all occurances of pattern in text in O(|text| + (num_occurances + 1)*|pattern|)."""
        positions = []
        
        # Precompute hash of pattern and x^|pattern| in O(|pattern|).
        x_p = functools.reduce(lambda aggregate, _: (aggregate * cls.x) % cls.p, range(len(pattern)), 1)
        pattern_hash = cls.poly_hash(s=pattern)
        
        # Compute rolling_hash once and check edge case for position = 0 in O(|pattern|).
        rolling_hash = cls.poly_hash(s=text[:len(pattern)])
        if rolling_hash == pattern_hash and text[:len(pattern)] == pattern:
            positions.append(0)
        
        # Iterate over O(|text|) positions, in each update rolling hash in O(1) using: H[k + 1] = H[k] * x + s[k + P] - s[k] * x^P (P = len(pattern)).
        for position in range(1, 1 + len(text) - len(pattern)):
            rolling_hash = (rolling_hash * cls.x + ord(text[position + len(pattern) - 1]) - ord(text[position - 1]) * x_p) % cls.p
            if rolling_hash == pattern_hash and text[position:position + len(pattern)] == pattern:  # O(1) unless hash match/collision, in which case O(|pattern|).
                positions.append(position)
        
        # Return positions of all occurances.
        return positions
        
    @classmethod
    def poly_hash(cls, s):
        """Compute the polynomial hash H = sum(s[0] * x^n + ... + s[n] * x^0) % p where n = len(s) - 1."""
        return functools.reduce(lambda aggregate, char: (aggregate * cls.x + ord(char)) % cls.p, s, 0)