
## add, mult operations
## each operator takes two arguments, another operation or a number
# input = string
# output = integer
    
## approach:
# process input
# process operand and its 2 arguments:
    # if either argument is another operator
        #then recurisvely call doMath to compute that result
    # else add or multiply the 2 numbers
    
#     "add ( mult (add 1 1) 3 ) 2 " => 8

#doMath([mult, 7, 2]) + doMath([2])

#takes in a part of the string, beginning with a '(', and finds the
# matching ')'
def findMatchingParen(restOfInputString):
    stack = []
    
    for i in range(0,len(restOfInputString)):
        
        if restOfInputString[i] == '(':
            stack.append('(')
        if restOfInputString[i] == ')':
            if len(stack) > 1:
                stack.pop()
                
            # the stack is size 1
            else:
                return i


#add ( mult 1 2 ) 3
#add 3 ( mult 1 2 )
#add ( add 1 2 ) ( mult 1 2 )
            

def doMath(inputString):
    

    
    operator = inputString[0]
    
    currentIndex = 1
            # case where argument 1 is an ( and operation needs to b done
    if inputString[currentIndex] == '(':

            # find the matching ')'
        closeParenIndex = findMatchingParen(inputString[currentIndex:])
        argument2Start = closeParenIndex+2
        print('Argument 2 should start at: ' + str(argument2Start))
        argument1 = doMath(inputString[currentIndex:closeParenIndex + 1])
        print ('argument 1 is: ' + str(argument1))
    # case where argument 1 is a number
    else:
        argument1 = inputString[currentIndex + 1]
        argument2Start = currentIndex + 1
    
    
    if inputString[argument2Start] == '(':
        secondCloseParenIndex = findMatchingParen(inputString[argument2Start+1:])

        argument2 = doMath(inputString[argument2Start:secondCloseParenIndex + 1])
        # figure out what argument 2 is, given argument 1 is an intege      
    else:
        argument2 = inputString[argument2Start]
    
    ## DO the operations
    if operator == "add":
        return int(argument1) + int(argument2)
    
    else:
        print argument1
        print argument2
        return int(argument1) * int(argument2)

            
        
        

            
            
            
            



            
    
    
    
    

    
    
def main():
    test = "add ( mult 1 3 ) 2"
    length = len(test) - 1
    inputString = test.split(" ")
    print doMath(inputString)
    

main()