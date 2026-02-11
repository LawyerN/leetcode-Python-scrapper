val[i] = max(nums[i], nums[i] + val[i+1])
#Where val[i] is the max sum of the subarray that starts from i (must include nums[i])