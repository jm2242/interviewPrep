class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        
        xBin = "{0:b}".format(x)
        yBin = "{0:b}".format(y)
        if len(xBin) < len(yBin):
            xBin = xBin.zfill( len(yBin) ) 
        elif len(yBin) < len(xBin):
            yBin = yBin.zfill( len(xBin) )
        

        dist = 0
        for i in range(len(xBin)):
            if xBin[i] != yBin[i]:
                dist += 1
        
        return dist
            
            

if __name__ == "__main__":
    sol = Solution()
    print sol.hammingDistance(1,4)
        