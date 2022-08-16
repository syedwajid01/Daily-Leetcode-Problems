class Solution:
    def firstUniqChar(self, s: str) -> int:
        sMap=Counter(s)
        
        for i in range(len(s)):
            if sMap[s[i]]==1:
                return i
        
        return -1
        