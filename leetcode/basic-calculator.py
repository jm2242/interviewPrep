NUMBERS = ["1","2","3","4","5","6","7","8","9", "0"]
OPERATORS = ['(',')','+','-']
PARENS = ['(',')']
ADD_SUB = ['+','-']
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.tokens = []
        self.parse(s)
        
        # create object to evaluate the RPN output
        evaluator = Evaluate()
        
        # set up required data structures
        op_stack = []
        out_queue = []
        
        # loop through tokens
        for token in self.tokens:
            
            # parse operator
            if self.isOperator(token):
                
                if token == '(':
                    op_stack.append(token)
                
                elif token in ADD_SUB:
                    # keep popping onto out queue until empty
                    while op_stack and self.equalOrLessPrec(token, op_stack[-1]):
                        out_queue.append(op_stack.pop())
                    
                    op_stack.append(token)
                    
            # parse number
            else:
                out_queue.append(token)
        print "out queue: {0}".format(out_queue)
        return evaluator.evalRPN(out_queue)          
                
                
            
            
        
   # parse input string into list of tokens 
    def parse(self,s):

        print "provided string {0}".format(s)

        # only valid input of length 1 is an integer
        if len(s) == 1:
            self.tokens.append(int(s))

        num = [] # use for parsing large integers

        for c1, c2 in zip(s, s[1:]+" " ):
            print c1, c2
            if c1 == " ":
                continue
            
            # if an operator
            if c1 in OPERATORS:
                self.tokens.append(c1)
                
            # at minimum c2 is a digit
            elif c1 in NUMBERS and c2 in NUMBERS:
                num.append(c1)
                
            # the last digit in the integer
            elif c1 in NUMBERS:
                num.append(c1)
                self.tokens.append(int(''.join(num)))
                num = []
        print "parsed string: {0}".format(self.tokens)
    
    # some basic helpers
    def isOperator(self, tok):
        return tok in OPERATORS
    
    # returns if op1 has less than or equal to precedence
    # over op2
    def equalOrLessPrec(self, op1, op2):
        if op1 in PARENS and op2 in ADD_SUB:
            return False
        else:
            True
        
        

class Evaluate(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return None
            
        self.tokens = tokens
        
        # convert all numbers to ints for simplicity
        self.processTokens()
        print self.tokens
        
        stack = []
        for token in self.tokens:
            if token not in OPERATORS:
                stack.append(token)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                res = self.compute(operand1, operand2, token)
                stack.append(res)
        return stack.pop()
            
    def compute(self, op1, op2, operator):
        if operator == '*':
            return op1 * op2
        elif operator == '/':
            return int(float(op1) / float(op2))
        elif operator == '+':
            return op1 + op2
        elif operator == '-':
            return op1 - op2
        else:
            raise Exception("unsupported operator")
    
    
    
    # convert all integers represented as strings to ints
    def processTokens(self):
        parsed_tokens = []
        for token in self.tokens:
            
            try:
                parsed_tokens.append(int(token))
                
            # if token is not a number (an operator likely) then just append it
            except ValueError:
                parsed_tokens.append(token)
        self.tokens = parsed_tokens
                    
        
        
if __name__ == "__main__":
    sol = Solution()
    test = "1 + 1"
    print sol.calculate(test)