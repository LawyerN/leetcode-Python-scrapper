class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        is_neg = False
        for i in xrange(32):
            counter = 0
            for num in nums:
                if (num >> i) & 1:
                    counter += 1
            
            if counter % 3 == 1:
                ans += pow(2, i)
                if i == 31:
                    is_neg = True
        return ans if not is_neg else ans - pow(2, 32)