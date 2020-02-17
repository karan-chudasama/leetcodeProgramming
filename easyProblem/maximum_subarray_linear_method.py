class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max_number = global_max_number = nums[0]
        
        nums = nums[1:]
        
        for i in nums:
            current_max_number = max(i, current_max_number+i)
            
            if current_max_number > global_max_number:
                global_max_number = current_max_number
        
        return global_max_number
