class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # operator only includes the addition , subtraction , multiplication and division
        #  for division if there are any decimal value, you should convert it into whole number

        # look for operator
        #  ["1","2","+","3","*","4","-"]
                  
        #  ["3","3","*","4","-"]
                     
        # ["9","4","-"]
                  

        
        while len(tokens) != 1:
            
        #  if operator is found , the the two operand before and apply the operator
            for i in range(len(tokens)):
                if tokens[i] in ('+','-','*','/'):
                    a = int(tokens[i-2])
                    b = int(tokens[i-1])
                    
                    if tokens[i] == '+':
                        result = a+ b
                    elif tokens[i] == '-':
                        result = a -b
                    elif tokens[i] == '*':
                        result = a*b
                    else :
                        result = int(a/b)
                    tokens = tokens[:i-2]+[str(result)] + tokens[i+1:]
                    break
            
  
        return int(tokens[0])

        # repalce the token list till end of the array
        # return the computed value