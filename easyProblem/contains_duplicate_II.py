class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dup_dict = {}
        
        for i, num in enumerate(nums):
            if num in dup_dict:
                if (i - dup_dict[num]) <= k:
                    return True
            dup_dict[num] = i
            
        return False
        
