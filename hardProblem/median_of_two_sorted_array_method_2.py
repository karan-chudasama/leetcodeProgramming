# Time Complexity O(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s1 = s2 = 0
        e1 = len(nums1) - 1
        e2 = len(nums2) - 1
        
        while True:
            numsleft = e1 - s1 + e2 - s2 + 2
            
            if numsleft <= 2:
                result = 0
                while s1<=e1:
                    result += nums1[s1]
                    s1 += 1
                while s2<=e2:
                    result += nums2[s2]
                    s2 += 1
                return result / 2 if numsleft == 2 else result
            
            if s1 <= e1 and s2 <= e2:
                min_num1 = nums1[s1]
                min_num2 = nums2[s2]
                
                if min_num1 < min_num2:
                    s1 += 1
                else:
                    s2 += 1
            elif s1 <= e1:
                s1 += 1
            else:
                s2 += 1
                
            if e1 >= s1 and e2 >= s2:
                max_num1 = nums1[e1]
                max_num2 = nums2[e2]
                
                if max_num1 > max_num2:
                    e1 -= 1
                else:
                    e2 -= 1
            elif e1 >= s1:
                e1 -= 1
            else:
                e2 -= 1
        
