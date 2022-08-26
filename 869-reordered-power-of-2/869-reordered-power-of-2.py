class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        '''
        For resulting number to be power of 2 , if we reorder the digits , then only one digit should be set 
          i.e n&(n-1)==0 
          
         
        2 4 8 16 32 64 128 256 ...
        1 2 4  8 16
        
        23/2 = 11  
        
        23%2 = 1 
        
        23 
        we can reorder the digits and we get power of 2 
        
        32
        
        
        
        
        '''
        
        c=Counter(str(n))
        
        return any(c==Counter(str(1<<i)) for i in range(31))
        
        
        
        