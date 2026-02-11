class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0

        out = 0  # Initialize output with \'0000...{32 times}...000\'
        for _ in range(31):
            bit = n & 1  # 1. Take the last bit of n 
            out |= bit   # 2. Set the last bit of output to the last bit of n 
            out <<= 1    # 3. Left shift output by 1 so that the last bit set is now one step to the left
            n >>= 1      # 4. Right shift n by 1 so that in the next iteration, we can extract the next bit
        
        # We set the 32nd bit outside of the loop because we don\'t want to left shift output after this.
        out |= n  
        return out