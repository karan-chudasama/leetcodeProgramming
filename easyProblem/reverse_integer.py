class Solution:
    def reverse(self, x: int) -> int:
        
        reversed_x = 0
        negate = 1
        if x < 0:
            negate = -1
        x = abs(x)
        
        while x>0:
            reversed_x = reversed_x * 10 + (x % 10)
            if not (-2**31 <= reversed_x <= 2**31-1):
                return 0
            x = x // 10
        
        return reversed_x * negate
        
