// The insert position is the index which element\u2019s value is greater or equal with target.
// So we scan linearly the array will find the answer.
class Solution {
    public int searchInsert(int[] nums, int target) {
        //Traverse all elements through the loop...
        for(int i = 0; i < nums.length; i++){
            if(nums[i] >= target)   return i;
        }
    return nums.length;
    }
}