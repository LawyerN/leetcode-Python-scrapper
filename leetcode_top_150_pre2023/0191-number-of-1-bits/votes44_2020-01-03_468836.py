class Solution:

    def hammingWeight(self, n: int) -> int:
        
        # Base case
        if n == 0 :
            return 0
        
        # General case:
        # hammingWeight(n) 
        # = hammingWeight(n / 2) + LSB 
        # = hammingWeight(n / 2) + odd bit 
        # = hammingWeight(n / 2) + ( n & 1)
        
        # Python\'s right shift operator is >>
        return (n & 1) + self.hammingWeight( n >> 1 )