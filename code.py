class Solution:
    def reverse(self, x: int) -> int:
        IMIN, IMAX = -2**31, 2**31 - 1
        rev=0
        s= -1 if x<0 else 1

        x=abs(x)
        while x>0:
            a=x%10  
            // Before updating rev, check if multiplying by 10 and adding the next digit would exceed INT_MAX.
            if rev>(IMAX-a)//10:
                return 0
            rev=rev*10+ a 
            x=x//10  
        return rev * s
        
