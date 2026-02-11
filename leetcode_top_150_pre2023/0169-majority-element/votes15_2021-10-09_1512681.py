int majorityElement(vector<int>& nums) {
	int candidate = nums[0], count = 1;

	for(int i = 1; i < nums.size(); ++i)
	{
		if(!count)
			candidate = nums[i];
		if(nums[i] == candidate)
			++count;
		else
			--count;
	}

	return candidate;
}