class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or strs[0] == "":
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        
        ''' 
        general procedure:
        Cycle through each index i of each string  in strs. If the first character of all the 
        strings match, we now have a prefix o
        each time we are running through the for loop, we are validating if prefix up to i works
        if we reach the end of the for loop, we know it does work 
        
        ''' 
        # since we're limited by shortest string in strs, we'll just use the length of the first string
        # as the max value for i
        for i in range(len(strs[0])+1):
  
            try:
                
                # choose the first string as the prefix, arbitrarily
                prefix = strs[0][:i+1]
                    
                for string in strs[1:]:
                    # if the string up to index i matches, then continue on
                    if string[:i+1] == prefix:
                        continue
                    # otherwise, we'll return the last prefix that matched
                    # if this occurs when i=0, then the prefix returned is an empty string
                    else:
                        return prefix[:i]
                # if we reached the end of the for loop, this means all of the strings up to index i matched
                # we can advance the prefix by 1

             
            # we accessed a string out of range, so this means we'll return the last prefix that matched 
            except IndexError:
                return prefix[:i]
              
        # didn't catch an error, return the prefix validated
        return prefix[:i]
                
                
            
def main():
    sol = Solution()
    strs = ["a","ab","abc"]
    print sol.longestCommonPrefix(strs)


                
if __name__ == "__main__":
    main()                
