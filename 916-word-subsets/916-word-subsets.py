class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        #convert all the word in words2 to single char map bmax
        bmax=[0]*26
        for word in words2:
            count=self.getCount(word)
            for i in range(26):
                bmax[i]=max(bmax[i],count[i])
        
        ans=[]
        
        for word in words1:
            count=self.getCount(word)
            isUniversal=True
            for i in range(26):
                if count[i]<bmax[i]:
                    isUniversal=False
                    break
            if isUniversal:
                ans.append(word)
                
        return ans
    
                
    
    
    
    
    def getCount(self,word):
        count=[0]*26
        for letter in word:
            count[ord(letter)-ord('a')]+=1
        
        return count
            
            
        