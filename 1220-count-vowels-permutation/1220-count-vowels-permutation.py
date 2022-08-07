from collections import defaultdict
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        '''
        
        n , how many string of length n can be formed 
        
        a e i o u 
        
        ae 
        
        ea ei 
        
        i i x
        
        oi ou
        
        ua
        
        if n is 1 return 5
        
        if n==2 
        
        a:["e"]
        e:["a","i"]
        i:["a","e","o","u"]
        o:["i","u"]
        u:["a"]
        
        [a e i o u]
        
        for i in range(2,n+1):
           newArr=["e","a","i","a",]
           for string in res:
              for followedChar in map[string[-1]]:
                newArr.append(stirng+followedChar)
           
                    
             
        '''
        if n==1:
            return 5
        
        vowels=["a","e","i","o","u"]
        
        followedBy={
        "a":["e"],
        "e":["a","i"],
        "i":["a","e","o","u"],
        "o":["i","u"],
        "u":["a"],
        }
        
        res={"a":1,"e":1,"i":1,"o":1,"u":1}
        
        for i in range(2,n+1):
            curr=defaultdict(int)
            for v in vowels:
                #if we have at least one char in the res
                if res[v]>=1:
                    #this char has to be followed by other chars
                    count=res[v]
                    # res[v]=0
                    #update curr
                    for char in followedBy[v]:
                        curr[char]+=count
            res=curr
        
        
        ans=0
        for key,val in res.items():
            ans+=val
        
        return ans%(10**9+7)
        
            
            
        
        
        