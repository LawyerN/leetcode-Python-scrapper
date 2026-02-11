def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = [1]*len(nums)
        res[-1] = 1
        for i in reversed(range(len(nums))):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    res[i] = max(res[i], res[j] + 1)
        return max(res)