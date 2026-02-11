def rotate(self, nums: List[int], k: int) -> None:
	n = len(nums) # store length of nums
	for _ in range(k):
		prev = nums[-1] # previous element starts as the end
		for i in range(n):
			nums[i], prev = prev, nums[i] # this element becomes the previous one, store this element in prev