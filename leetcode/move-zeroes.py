class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # keep a pointer i to the first 0 element from the left
        i = 0
        
        # advance i until it points to the first 0 element
        while i < len(nums):
            if nums[i] != 0:
                i += 1
                continue
            else:
                break
        print i 
       
        j = i + 1
        
        # advance a pointer j until a non-zero element is encountered
        while j < len(nums):

            # swap if element at j isn't 0
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
    
            j += 1
              
        return nums    
            
            
 



        # crappy O(n^2) bubble sort inspired solution 
         # if not nums:
        #     return []

        # # number of zeros, use to keep track how many zeros adjusted
        # zeroCount = nums.count(0)
        # zerosAdjusted = 0
        # idx = 0

        # while zeroCount > 0:
        #     print nums
        #     if nums[idx] != 0:
        #         idx += 1
        #         continue
            
        #     # swap 0 to the back
        #     j = idx + 1
        #     i = idx
        #     while j < len(nums) -zerosAdjusted :
        #         nums[i],nums[j] = nums[j], nums[i]
        #         j += 1
        #         i += 1
        #     idx = 0
        #     zeroCount -= 1
        #     zerosAdjusted += 1
        # return nums    

                
        
if __name__ == "__main__":
    sol = Solution()
    test = [0,1,0,3,12]
    print "running: {0}".format(test)
    print sol.moveZeroes(test)