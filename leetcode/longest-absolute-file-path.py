class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        
        if not input:
            return 0
            
        
        maxLength = 0
        stack = SimpleStack()
        input = input.split('\n')
        

        
        for line in input:
            print stack
            print ""
            print "processing line:"
            print line
            
            # get the indent amount strip the tabs
            tab_count = line.count("\t")
            space_count = line.count(" ")

            # hack needed becauses input sometimes has 4 spaces instead of a tab character
            # test cases are dumb, only the first 4 four spaces are considered to tabs, the
            # rest are actually part of the file name

            if tab_count >  0:
                line = line.strip("\t")
                cur_indent = tab_count
            elif space_count >= 4:
                line = (space_count - 4) * " " + line.strip(" ")
                cur_indent = 1
            else:
                cur_indent = 0

            line = line.strip("\t")
            # the line is a file with an extension, and not a directory
            if '.' in line:
                
                # if we're indented, then we'll take the length of the current subdirectory
                # + the length of the current line
                if stack.indent() == 0:
                    pass

                elif cur_indent > stack.indent():
                    pass
                    
                # if we're on the same level as the current subdirectory
                elif cur_indent == stack.indent():
                    stack.pop()
                
                # if the indent level is less than indent so far
                elif cur_indent < stack.indent():
                    # push lines off of the stack until the we are at the same level as the current line
                    while cur_indent <= stack.indent():
                        stack.pop()
                    
                # get the length
                length = stack.peekLength() + len(line)
                print "computed length: {0}".format(len(line))
                # check if there is a new max length
                if length > maxLength:
                    maxLength = length
                    
            # line is a subdirectory 
            else:
                # add a "/" character to the end of each subdirectory
                line += "/"
                
                # multiple cases

                # if there is not root level directory currently
                if cur_indent == 0:
                    stack.clear()

                # if the indent level is the same, pop old directory and push new
                elif  cur_indent == stack.indent():
                    stack.pop()
  
                # if the indent level is less than indent so far
                elif cur_indent < stack.indent():
                    
                    # push lines off of the stack until the we are at the same level as the current line
                    while cur_indent <= stack.indent():
                        stack.pop()

                    
                # if indent level is 1 greater, push new
                elif cur_indent == stack.indent() + 1: 
                    pass
                
                # impossible state, throw error
                else:
                    raise Exception("improper directory structure")

                stack.push(line)
            print "------------"
        return maxLength        


class SimpleStack:
    def __init__(self):
        self.lines = []
        self.lengths = []

    def __str__(self):
        str1 =  "lines: {0}".format(self.lines)
        str2 =  " lengths: {0}".format(self.lengths)
        str3 = " current indent: {0}".format(self.indent())
        return str1 + str2 + str3


    
    # push the line onto self.lines and the length of line onto self.
    def push(self, line):
        
        # if empty, length is 0
        if self.isEmpty():
            _currentLength = 0
        else:
            _currentLength = self.lengths[-1]
        
        self.lines.append(line)
            
        self.lengths.append(_currentLength + len(line))
    
    # empties the stack completely
    def clear(self):
        self.lines = []
        self.lengths = []


    def pop(self):
        if not self.isEmpty():
            # raise IndexError("trying to pop from an empty stack")
            self.lengths.pop()
            self.lines.pop()
    
    # return the indent level of the current state of the stack
    # consider indent based on number of tabs, no tabs = 0 indent
    # if stack is empty, indent = -1
    def indent(self):
        if self.isEmpty():
            return -1

        return len(self.lines) - 1
    
    def peekLength(self):
        if self.isEmpty():
            return 0
        else:
            return self.lengths[-1]
    
    def peekLine(self):
        if self.isEmpty():
            return 0
        else:
            return self.lines[-1]
        
    def isEmpty(self):
        return not self.lines
        

def main():
    sol = Solution()
    tests = ["dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext", \
    "a\n\taa\n\t\taaa\n\t\t\tfile1.txt\naaaaaaaaaaaaaaaaaaaaa\n\tsth.png", "dir\n    file.txt", \
    "dir\n        file.txt", "dir\n\t        file.txt\n\tfile2.txt", "a\n\tb.txt\na2\n\tb2.txt"]
    for test in tests:
        print sol.lengthLongestPath(test)


if __name__ == "__main__":
    main()
