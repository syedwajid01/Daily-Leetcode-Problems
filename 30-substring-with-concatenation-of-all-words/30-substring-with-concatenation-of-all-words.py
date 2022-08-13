from collections import *
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        m=len(words[0])
        n=len(words)
        wordsMap=Counter(words)
        windowLen=m*n
        required=len(wordsMap)
        windowStart=0
        ans=[]
        
        for windowEnd in range(windowLen-1,len(s)):
            currWordsMap=defaultdict(int)
            formed=0
            currIdx=windowStart
            
            for i in range(n):
                currWord=s[currIdx:currIdx+m]
                if currWord in wordsMap:
                    currWordsMap[currWord]+=1
                    if currWordsMap[currWord]==wordsMap[currWord]:
                        formed+=1
                else:
                    break
                currIdx+=m
            
            if formed==required:
                ans.append(windowStart)
    
            windowStart+=1
        
        return ans
                    
                    
                
            
        