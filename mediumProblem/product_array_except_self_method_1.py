class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        max_product = 1
        
        for i in nums:
            max_product *= i
            
        for i, num in enumerate(nums):
            nums[i] = max_product // num
            
        return nums
        
