class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_product = [0] * len(nums)
        right_product = [0] * len(nums)
        
        # create left product list first
        left_product[0] = 1
        for i in range(1, len(nums)):
            left_product[i] = left_product[i-1] * nums[i-1]
            
        # create right product list
        right_product[len(nums)-1] = 1
        for i in reversed(range(len(nums)-1)):
            right_product[i] = right_product[i+1] * nums[i+1]
            
        new_nums = [0] * len(nums)
        for i in range(len(nums)):
            new_nums[i] = left_product[i] * right_product[i]
            
        return new_nums
        
