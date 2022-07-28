class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        
        tmap=[0]*26
        smap=[0]*26
        
        for i in range(len(s)):
            tmap[ord(t[i])-ord("a")]+=1
            smap[ord(s[i])-ord("a")]+=1
        
        for i in range(26):
            if tmap[i]!=smap[i]:
                return False
        
        return True
            
        