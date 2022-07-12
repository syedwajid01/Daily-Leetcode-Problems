class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def generate(openBrackets,closeBrackets,curr):
            if openBrackets==closeBrackets==n:
                ans.append(curr[:])
                return
            
            if openBrackets<n:
                generate(openBrackets+1,closeBrackets,curr+"(")
            
            if openBrackets>closeBrackets:
                generate(openBrackets,closeBrackets+1,curr+")")
        
        generate(0,0,"")
        return ans
        
        
                
        