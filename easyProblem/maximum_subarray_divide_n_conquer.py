class Solution:
    
    def findMaxSubarray(self, nums, low, high):
        
        if low == high:
            return low, high, nums[low]
        mid = (low + high) // 2
        
        left_low, left_high, left_max = self.findMaxSubarray(nums, low, mid)
        right_low, right_high, right_max = self.findMaxSubarray(nums, mid+1, high)
        cross_low, cross_high, cross_max = self.findMaxCrossSubarray(nums, low, mid, high)
        
        if left_max >= right_max and left_max >= cross_max:
            return left_low, left_high, left_max
        elif right_max >= left_max and right_max >= cross_max:
            return right_low, right_high, right_max
        else:
            return cross_low, cross_high, cross_max
        
    def findMaxCrossSubarray(self, nums, low, mid, high):
        left_max = float("-inf")
        left_high = mid
        left_sum = 0
        for i in range(mid, low, -1):
            left_sum += nums[i]
            if left_sum > left_max:
                left_max = left_sum
                left_high = i
                
        right_max = float("-inf")
        right_high = mid+1
        right_sum = 0
        for i in range(mid+1, high):
            right_sum += nums[i]
            if right_sum > right_max:
                right_max = right_sum
                right_high = i
                
        return left_high, right_high, left_max + right_max
    
    def maxSubArray(self, nums: List[int]) -> int:
        
        return self.findMaxSubarray(nums, 0, len(nums)-1)[-1]
