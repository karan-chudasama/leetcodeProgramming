# Time Complexity O(min(m, n))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num1, num2 = nums1, nums2
        if len(num1) > len(num2):
            num1, num2 = num2, num1
            
        l_num1 = len(num1)
        l_num2 = len(num2)
        
        start = 0
        end = l_num1
        pos_x = 0
        pos_y = 0
        
        while(start <= end):
            pos_x = (start + end) // 2
            pos_y = ((l_num1 + l_num2 + 1) // 2) - pos_x
            
            if pos_x == 0:
                maxleftnum1 = float("-inf")
            else:
                maxleftnum1 = num1[pos_x-1]
            
            if pos_x == l_num1:
                minrightnum1 = float("inf")
            else:
                minrightnum1 = num1[pos_x]
                
            if pos_y == 0:
                maxleftnum2 = float("-inf")
            else:
                maxleftnum2 = num2[pos_y-1]
                
            if pos_y == l_num2:
                minrightnum2 = float("inf")
            else:
                minrightnum2 = num2[pos_y]
                
            if (maxleftnum1 <= minrightnum2 and maxleftnum2 <= minrightnum1):
                if(l_num1 + l_num2)%2==0:
                    return (max(maxleftnum1, maxleftnum2) + min(minrightnum1, minrightnum2)) / 2
                else:
                    return max(maxleftnum1, maxleftnum2)
            elif maxleftnum1 > minrightnum2:
                end = pos_x - 1
            else:
                start = pos_x + 1
