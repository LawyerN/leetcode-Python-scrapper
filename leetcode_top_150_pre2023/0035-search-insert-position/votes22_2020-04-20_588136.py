lo = 0
hi = len(nums) - 1

while lo <= hi:
	mid = (lo + hi) // 2
	if target <= nums[mid]:
		hi = mid - 1
	else:
		lo = mid + 1

return lo