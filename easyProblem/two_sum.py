class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        
        for i, num in enumerate(nums):
            if (target-num) in result:
                return [result[target-num], i]
            result[num] = i
            
