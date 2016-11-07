class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = 2
        w = 0
        while(r<=len(height)-1):
            counter = 1
            flag = True
            print(l,r)
            while(height[l]>height[(l+r)/2] and height[l]>height[(l+r)/2]):
                print("left",l,height[l])
                print ("middle",((l+r)/2),height[(l+r)/2])
                print("right",r,height[r])
                flag = False
                print (counter*2-1)
                w+=(counter*2-1)
                counter+=1
                r+=2
                print(w)
            if flag:
                print("not trap")
                print(l,r)
                l+=1
                r+=1
            else:
                print("trap")
                print(l,r)
                l += (counter-1)*2
                r = l + 2
        return w

if __name__ == "__main__":
    solution = Solution()
    test  = [0,1,0,2,1,0,1,3,2,1,2,1]
    print solution.trap(test)
