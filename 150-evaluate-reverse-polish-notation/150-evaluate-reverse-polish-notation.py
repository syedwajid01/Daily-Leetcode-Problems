class Solution:
    def isOperator(self,token):
        operators={"+","-","*","/"}
        return token in operators

    
    def evaluate(self,num1,num2,op):
        if op=="+":
            return num1+num2
        elif op=="-":
            return num1-num2
        elif op=="*":
            return num1*num2
        else:
            return int(num1/num2)
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        
        for token in tokens:
            if self.isOperator(token):
                num2=stack.pop()
                num1=stack.pop()
                res=self.evaluate(num1,num2,token)
                stack.append(res)
            else:
                stack.append(int(token))
        
        return stack[0]
            
        