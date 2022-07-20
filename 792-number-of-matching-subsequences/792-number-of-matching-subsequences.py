class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        '''
        
        s= "abcde"
        
        words = ["a","bb","acd","ace"]
        
        for every word in words:
            check if word is subseq of string s 
            
        w = len(words)
        
        slen= len(s)
        
        wordlen=len(word)
        
        w*(slen+wordlen)
        
        for letter in word
        
        '''
        
        hashmap=collections.defaultdict(list)
        ans=0
        
        for word in words:
            firstLetter=word[0]
            restOfTheWord=word[1:]
            hashmap[firstLetter].append(restOfTheWord)
        
        for letter in s:
            words_waiting=hashmap.pop(letter,[])
            
            for word in words_waiting:
                if len(word)==0:
                    ans+=1
                    continue
                nextLetter=word[0]
                restOfTheWord=word[1:]
                hashmap[nextLetter].append(restOfTheWord)
                
        return ans
                
        