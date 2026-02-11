class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum=nums[0]
        minSize= sys.maxsize
        i,j=0,0
        while j<len(nums) and i<len(nums):
            if sum<target:
                j=j+1
                if j==len(nums): break
                sum=sum+nums[j]
            elif sum>=target:
                if j-i+1<minSize: minSize=j-i+1
                sum=sum-nums[i]
                i=i+1
        return 0 if minSize== sys.maxsize else minSize