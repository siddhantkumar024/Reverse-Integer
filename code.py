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




explain ------

Sure — let’s break down

Python

Copy code
if rev > (INT_MAX - digit) // 10:
with an example so you see why it prevents overflow.

Background
We are reversing an integer digit-by-digit.
At each step:


Copy code
rev = rev * 10 + digit
If rev is already large enough that multiplying by 10 and adding digit would exceed INT_MAX (2,147,483,647), we must stop and return 0.

Example:
Let’s reverse 1534236469 (which will overflow a 32-bit signed int).

Step before overflow:


Copy code
rev = 964632435
digit = 1
INT_MAX = 2147483647
Check:


Copy code
(INT_MAX - digit) // 10
= (2147483647 - 1) // 10
= 2147483646 // 10
= 214748364
Compare:


Copy code
rev = 964632435
limit = 214748364
rev > limit  →  True
Since 964632435 > 214748364,
if we did rev * 10 + digit, we’d get:


Copy code
964632435 * 10 + 1 = 9646324351  (way bigger than 2,147,483,647)
So we return 0 instead of overflowing.

✅ In short:
(INT_MAX - digit) // 10 is the largest safe value rev can have before adding the next digit.
If rev is bigger than that, the next step will overflow.
        
