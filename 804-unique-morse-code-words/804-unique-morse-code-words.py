class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCode=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        transformations=set()
        
        for word in words:
            wordMorseCode=""
            for letter in word:
                idx=ord(letter)-ord("a")
                wordMorseCode+=morseCode[idx]
            transformations.add(wordMorseCode)
        
        return len(transformations)
            
        