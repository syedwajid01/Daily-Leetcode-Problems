class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        #given pattern
        #pattern me we have different letters 
        #abb
        #bab
        #abab
        #something like this
        #we need to map a ->
        
        patternLetterMap={}
        wordLetterPatternMap={}
        ans=[]
        
        for word in words:
            patternLetterMap={}
            wordLetterPatternMap={}
            followsPattern=True
            for i in range(len(word)):
                #map current letter in pattern with this word letter
                patternLetter=pattern[i]
                wordLetter=word[i]
                
                #if current pattern letter is already mapped with one of the word letter 
                #then curr word letter should be similar to that letter
                if patternLetter in patternLetterMap:
                    if wordLetter != patternLetterMap[patternLetter]:
                        followsPattern=False
                        break
                    continue
                
                #two patternLetters can not map to same wordLetter 
                #check is wordLetter is already mapped with any pattern letter previosly 
                #if yes then that wordLetter pattern should be similar to curr pattern 
                if wordLetter in wordLetterPatternMap and wordLetterPatternMap[wordLetter]!=patternLetter:
                    followsPattern=False
                    break
                
                patternLetterMap[patternLetter]=wordLetter
                wordLetterPatternMap[wordLetter]=patternLetter

            if followsPattern:
                ans.append(word)
        
        return ans
                
                    
                    
        