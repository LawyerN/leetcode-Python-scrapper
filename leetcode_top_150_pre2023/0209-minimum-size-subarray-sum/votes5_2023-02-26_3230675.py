class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target == 0 or not len(nums):
            return 0

        n = len(nums)
        minLen = float("inf")
        sums = [nums[0]]

        for i in range(1, n):
            sums.append(sums[i-1] + nums[i])

        for i in range(0, n):
            left = i
            right = n-1
            newTarget = target + sums[i] - nums[i]

            while left <= right:
                mid = (left + right) // 2
                if sums[mid] < newTarget:
                    left = mid + 1
                else:
                    right = mid - 1

            if left < n and sums[left] >= newTarget:
                minLen = min(minLen, left - i + 1)

        return 0 if minLen == float("inf") else minLen