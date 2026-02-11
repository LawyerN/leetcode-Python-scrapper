int removeDuplicates(vector<int>& nums) {        
	int numOfDuplicates = 0;

	for(int i = 1; i < nums.size(); ++i)
	{
		if(nums[i] == nums[i - 1])
			++numOfDuplicates;
		else
			nums[i - numOfDuplicates] = nums[i];
	}
	return nums.size() - numOfDuplicates;
}