class Solution:
    def romanToInt(self, s: str) -> int:
        romanToIntMap={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        i=0
        ans=0
        while i<len(s):
            if (i+1<len(s) and romanToIntMap[s[i]]>=romanToIntMap[s[i+1]]) or (i==len(s)-1):
                ans+=romanToIntMap[s[i]]
                i+=1
            elif i+1<len(s):
                ans+=(romanToIntMap[s[i+1]]-romanToIntMap[s[i]])
                i+=2
        
        return ans
        
        
                
            
        