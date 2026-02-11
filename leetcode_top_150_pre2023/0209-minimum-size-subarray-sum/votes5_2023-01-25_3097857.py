class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        maxi=sys.maxsize
        sums=0
        n=len(nums)
        while(j<n):                             #iterate until j reaches to the last element of the nums list
            
            sums+=nums[j]                  #calculation of sum using elements included in window
			while sums>=target:         #iterate until the value of sum is greater than target
                maxi=min(maxi,j-i+1)   #store the minimal value 
                sums-=nums[i]
                i+=1
            j+=1

        return maxi if maxi!=sys.maxsize else 0