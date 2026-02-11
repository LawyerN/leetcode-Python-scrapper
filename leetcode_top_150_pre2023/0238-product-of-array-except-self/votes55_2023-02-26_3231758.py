class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    left_product = [1] * n # initialize left_product array with 1
    right_product = [1] * n # initialize right_product array with 1
    # calculate the product of elements to the left of each element
    for i in range(1, n):
        left_product[i] = left_product[i - 1] * nums[i - 1]

    # calculate the product of elements to the right of each element
    for i in range(n - 2, -1, -1):
        right_product[i] = right_product[i + 1] * nums[i + 1]

    # calculate the product of all elements except nums[i]
    result = [left_product[i] * right_product[i] for i in range(n)]

    return result