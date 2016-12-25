import unittest

class Solution(object):

    # first go at an implementation
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        length = len(str)
        
        if length == 1:
            return False
        
        
        for idx, c in enumerate(str[:length/2]):
            substring = str[:idx+1]
            
            if length/(idx+1)*substring == str:
                return True
            
        return False

    # short, clever solution
    def repeatedShort(self,str):
        return str in (str+str)[-1:1]
        

def main():
    solution = Solution()



if __name__ == "__main__":
    main()