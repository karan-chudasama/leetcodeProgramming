class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg_sum = 0
        
        for row in grid:
            l = 0
            h = len(row) - 1
            
            while(l<=h):
                mid = (l+h)//2
                if(row[mid] < 0):
                    neg_sum += (h-mid+1)
                    h = mid - 1
                    
                if row[mid] >= 0:
                    l = mid + 1
                
        return neg_sum
