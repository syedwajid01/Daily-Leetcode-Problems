class Solution:
    def minDeletions(self, s: str) -> int:
        charFreqMap=Counter(s)
        
        seen_freq=set()
        ans=0
        for char,freq in charFreqMap.items():
            if freq in seen_freq:
                while freq!=0:
                    freq-=1
                    if freq not in seen_freq:
                        seen_freq.add(freq)
                        break
                ans+=charFreqMap[char]-freq
            else:
                seen_freq.add(freq)
        
        return ans
        