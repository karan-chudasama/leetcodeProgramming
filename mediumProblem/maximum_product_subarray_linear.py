class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max_product = current_min_product = max_product = nums[0]
        
        for i in range(1, len(nums)):
            temp = current_max_product
            current_max_product = max(nums[i], max(current_max_product*nums[i], current_min_product*nums[i]))
            
            current_min_product = min(nums[i], min(temp*nums[i], current_min_product*nums[i]))
            
            max_product = max(max_product, current_max_product)
                
        return max_product
        
