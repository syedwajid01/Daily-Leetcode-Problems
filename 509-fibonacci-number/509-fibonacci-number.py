class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        first=0
        second=1
        for i in range(2,n+1):
            temp=first+second
            first=second
            second=temp
        
        return second
        