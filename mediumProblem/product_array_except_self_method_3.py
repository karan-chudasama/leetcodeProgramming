class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_nums = [0] * len(nums)
        
        # prepare left product list first
        product_nums [0] = 1
        for i in range(1, len(nums)):
            product_nums[i] = nums[i-1] * product_nums[i-1]
            
        # maintain right product in variable instead of list
        right_product = 1
        for i in reversed(range(len(nums))):
            product_nums[i] = product_nums[i] * right_product
            right_product *= nums[i]
        
        return product_nums
