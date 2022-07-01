class Solution:
    def operate(self,a,b,token):
        if token == "/":
            return int(b / a)
        elif token == "*":
            return a * b
        elif token == "+":
            return a + b
        elif token == "-":
            return b - a
    
    def isSymbol(self,token):
        tokens = {"/","+","-","*"}
        return token in tokens
            
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for token in tokens:
            
            if self.isSymbol(token):
                a = stack.pop()
                b = stack.pop()
                c = self.operate(a,b,token)
                stack.append(c)
                
            else:
                stack.append(int(token))
                
        return stack[0]