class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        nums = str(x)
        
        i = 0
        j = len(nums) - 1
        
        while i <= j:
            if nums[i] != nums[j]:
                return False
            i += 1
            j -= 1
        return True