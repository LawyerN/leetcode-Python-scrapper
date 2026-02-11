class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
            This question can be solved using bit manipulation.
            If any number is occuring 3 times then the count of every set bit of that number will also be 3.
            For example, let\'s say we have 5,5,5 then,
            Binary representation is 101,101,101.
            We can see that the count of 0th and 2nd bit will be 3.
            Now if another number comes, let\'s say 4(100) then the count of every set bit will be:
                0th: 3
                2nd: 4
            
            So by using the above logic if we get a count of each set bit for all the numbers and take modulo of 3 for each bit then the resulting number would be our answer.
            Like in above example, count of each bit became 4, 0, 3 and if we take % 3 then it will become 1,0,0 and 100 is 4(our answer).
            
        """
        res = 0
        for i in range(32):
            count = 0
            for n in nums:
                temp = n >> i
                temp = temp & 1
                count += temp
            rem = count % 3
            if i == 31 and rem:  # must handle the negative case
                res -= 1 << 31
            else:
                res |= rem << i
        return res