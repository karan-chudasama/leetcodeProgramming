class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        counter = 1
        
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[counter] = nums[i]
                counter += 1
                
        return counter
            
        
