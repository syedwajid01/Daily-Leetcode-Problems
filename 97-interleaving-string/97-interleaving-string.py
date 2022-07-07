class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        lenS1,lenS2,lenS3=len(s1),len(s2),len(s3)
        
        if lenS1+lenS2!=lenS3:
            return False
        
        self.mp={}
        return self.solve(s1,s2,s3,lenS1,lenS2,lenS3)
        
    
    
    def solve(self,s1,s2,s3,s1Idx,s2Idx,s3Idx):
        if s3Idx<=0:
            return True
        
        s1Res=False
        s2Res=False
        
        key=(s1Idx,s2Idx)
        
        if key in self.mp:
            return self.mp[key]
        
        if s1Idx>0 and  s1[s1Idx-1]==s3[s3Idx-1]:
            s1Res = self.solve(s1,s2,s3,s1Idx-1,s2Idx,s3Idx-1)
            if s1Res:
                return True
        
        if s2Idx>0 and s2[s2Idx-1]==s3[s3Idx-1]:
            s2Res = self.solve(s1,s2,s3,s1Idx,s2Idx-1,s3Idx-1)
            if s2Res:
                return True
        
        
        self.mp[key] = s1Res or s2Res
            
            
        