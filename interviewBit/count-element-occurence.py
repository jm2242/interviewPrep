class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        return self.binary_search(list(A), B)
     
     
    def countOccurences(self, mid, nums, length, elem):
        accum = 1
        
        # count down from mid first 
        i = mid - 1
        while i >=0 and nums[i] == elem:
            accum += 1
            i -= 1
        

        # count up from mid
        i = mid + 1
        while i < length and nums[i] == elem:
            accum += 1
            i += 1

        return accum    
       
    def binary_search(self, nums, elem, length=None):
        low = 0
        
        
        if length is None:
            length = len(nums)
            high = length - 1
        else:
            high = length - 1
    
        # exit loop when low is either high or greater, depending on if odd or even
        # number of elements
        while low <= high:
            # get the middle 
            mid = low + (high - low) / 2
            if nums[mid] == elem:
                return self.countOccurences(mid,nums, length, elem)
            elif nums[mid] > elem:
                high = mid - 1
            elif nums[mid] < elem:
                low = mid + 1
        
        else:
            return 0

def main():
    sol = Solution()
    nums = [1,1,2,2,3,4,5,6,7]
    print sol.findCount(nums, 7)


if __name__ == "__main__":
    main()