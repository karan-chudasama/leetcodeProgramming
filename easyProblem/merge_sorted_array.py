class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        max_end = m + n - 1
        num1_end = m - 1
        num2_end = n - 1
        
        while (num1_end >= 0 and num2_end >= 0):
            
            if nums1[num1_end] > nums2[num2_end]:
                nums1[max_end] = nums1[num1_end]
                max_end -= 1
                num1_end -= 1
            else:
                nums1[max_end] = nums2[num2_end]
                max_end -= 1
                num2_end -= 1
                
        while num2_end >=0:
            nums1[max_end] = nums2[num2_end]
            max_end -= 1
            num2_end -= 1
