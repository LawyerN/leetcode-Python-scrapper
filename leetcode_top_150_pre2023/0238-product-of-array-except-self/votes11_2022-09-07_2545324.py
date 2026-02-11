class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        for example:
            nums = [a, b, c, d]
        we want
            res = [bcd, acd, abd, bcd]
        """
        res = [1] * nums
        product = 1

        """
        after that, we get
            res = [1, a, ab, abc]
        """
        for i, num in enumerate(nums):
            res[i] *= product
            product *= num

        """
        from
            res  = [1, a, ab, abc]
            nums = [a, b, c, d]
        to
            res = [1 * dcb, a * dc, ab * d, abc * 1]
                = [bcd, acd, abd, abc]
        """
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= product
            product *= nums[i]

        return res