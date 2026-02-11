class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            mask = 1<<i
            
            count = 0
            for num in nums:
                if num&mask:
                    count += 1
            
            if count%3:
                if i == 31:
                    print(ans, mask)
                    ans -= mask
                else:
                    ans |= mask
        
        return ans