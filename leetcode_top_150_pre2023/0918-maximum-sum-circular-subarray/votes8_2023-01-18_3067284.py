class Solution:
    def maxSubarraySumCircular(self,nums: list[int]) -> int:

                                                     #  Example: nums = [-2, 7, 5, -3, 5, 1] 
        n, sm, ans = len(nums), sum(nums), max(nums) #
        mx, tmpMx, mn, tmpMn = -inf, 0, 0, inf       #   num    mx  tmpMx   mn    tmpMx
                                                     #   ---   ---   ---   ---    ---     
        for num in nums:                             #         -inf   0     0     inf 
                                                     #   -2      0    0     0      0
            tmpMx+= num                              #    7      7    7     0      0 
            mx, tmpMx = max(mx,tmpMx), max(0,tmpMx)  #    5     12    9    -3     -3
                                                     #
            tmpMn+= num                              #   -3     14   14    -3     -3
            mn, tmpMn = min(mn,tmpMn), min(0,tmpMn)  #    5
                                                     #   -1     15   15    -3     -3

        return max(mx, sm - mn)                      #   max(mx, sm - mn) = max(15, 13-(-3))
                                                     #                    = 16 <-- answer