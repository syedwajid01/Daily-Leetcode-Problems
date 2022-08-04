class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        #m*p = n*q 
        # if n == number of reflections +1 
        # m= number of extended cubes  +1 
        # if no of reflections is even then receptor is on right side
        #else receptor is on left side 
        
        #m is even & n is odd => return 0.
        #m is odd & n is odd => return 1.
        #m is odd & n is even => return 2.
        while p%2==0 and q%2==0:
            p,q=p//2,q//2
            
        return 1 - p % 2 + q % 2
        
        