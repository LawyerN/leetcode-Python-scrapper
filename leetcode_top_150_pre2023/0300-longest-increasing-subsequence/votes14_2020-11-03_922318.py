def dfs(nums, prev):
	if not nums:
		return 0
	longest = 0
	for i in range(len(nums)):
		if nums[i] > prev:
			curr = 1 + dfs(nums[i + 1:], nums[i])
			longest = max(longest, curr)
	return longest
return dfs(nums, -float("inf"))