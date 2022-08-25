class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineMap=Counter(magazine)
        
        for letter in ransomNote:
            if letter not in magazineMap:
                return False
            magazineMap[letter]-=1
            if magazineMap[letter]<0:
                return False
        
        return True
        