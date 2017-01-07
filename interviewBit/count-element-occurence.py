class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    
     

    def binary_search(self, nums, elem, length=None, kind="base"):
        low = 0
    
        result = None
        kind = kind.lower()
        if kind not in ("base", "first", "last"):
            raise TypeError("invalid binary search type")
    
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
    
                # if normal binary search, just return the first index found
                if kind == "base":
                    return mid
                elif kind == "first":
                    result = mid
                    high = mid - 1
                elif kind == "last":
                    result = mid
                    low = mid + 1
            elif nums[mid] > elem:
                high = mid - 1
            elif nums[mid] < elem:
                low = mid + 1
    
        else:
            return result
    
    def occurrences(self, nums, elem):
        length = len(nums)
        last = self.binary_search(nums, elem, length, "last")
        first = self.binary_search(nums, elem, length, "first")
        if last is None:
            return 0
        return last - first + 1
    def findCount(self, A, B):
        return self.occurrences(A,B)
     
    
    



def main():
    sol = Solution()
    nums = [1,1,2,2,3,4,5,6,7]
    print sol.findCount(nums, 7)


if __name__ == "__main__":
    main()