import math
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        '''
        
        (T+1)^p<=N 
        
        plog(T+1)=log(N)
        
        p=
        
        '''
        T=minutesToTest/minutesToDie
        
        return math.ceil(math.log(buckets)/math.log(T+1))