class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n>1:
            n/=4
            
        return n==1
        