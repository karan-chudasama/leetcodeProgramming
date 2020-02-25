class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        pivot = 0
        
        while(low<high):
            mid = (low+high)//2
            
            if nums[low] < nums[high]:
                pivot = 0
                break
            
            if nums[mid] < nums[mid-1]:
                pivot = mid
                break
            if nums[mid] > nums[mid+1]:
                pivot = mid+1
                break
            if nums[mid] > nums[0]:
                low = mid+1
            else:
                high = mid
                
        low = 0
        high = len(nums) - 1
        while(low<=high):
            if nums[pivot] == target:
                return pivot
            if target >= nums[pivot] and target <= nums[high]:
                low = pivot + 1
            else:
                high = pivot - 1
                
            pivot = (low+high)//2
            
        return -1
        
        
