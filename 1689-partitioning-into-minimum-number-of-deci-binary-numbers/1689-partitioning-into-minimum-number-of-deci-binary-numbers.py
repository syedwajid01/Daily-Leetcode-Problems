class Solution:
    def minPartitions(self, n: str) -> int:
        '''
        
        input: string n 
        
        if n is single digit or <=9
        example n=8
        we will have to add 8 1's to get 8 
        so for single digit our answer will be that digit 
        
        if number > 9 or multi digit 
        
        example: 
        32
        then we will add
        11
        11
        10
        
    
        example: 
        82734
        
        11111
        11111
        10111
        10101
        10100
        10100
        10100
        10000
        
        as you can see for for multiple digits we need to do the same i.e have as many ones as that digit
        then group together
        
        so our answer will be the max digit in the given string (greedy approach)
        

        '''
        
        return int(max(n))
        