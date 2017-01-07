import sys
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        # sub_list_len = len(A[0])
        # return ([m[sub_list_len/2] for m in A].sort())[len(A)/2]
        l =0
        h = sys.maxint
        m = None
        target = (len(A) * len(A[0]) / 2)
        print "target: {0}".format(target)
        while (h - l) > 1:
            print "h: {0}".format(h)
            print "l: {0}".format(l)
            
            # shortened to distinguish from variables in binary search
            prevM = m
            m = l + (h - l) / 2
            # print m
            
            # keep track of the number of numbers less than mid
            count = 0
            for row in A:
                count += self.binary_search(row, m)
            print "count for {0} : {1} ".format(m, count)
            if count == target:
                return m
            elif count > target:
                h = m - 1
            elif count < target:
                l = m + 1
        
        if count > target:
            return prevM
        else:
            return m
            
                
            
        
        
    # slightly modified binary search to return number of elements
    # that are smaller than elem 
    def binary_search(self, nums, elem, length=None):
        low = 0
        
        count = 0
        
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
            
            # return the count of numbers less than element
            if nums[mid] == elem:
                return mid
                
            elif nums[mid] > elem:
                high = mid - 1
            elif nums[mid] < elem:
                low = mid + 1
        
        # return whether we are the bottom or top of the list
        # tells us whether the number is too small or too large
        else:
            if nums[mid] < elem:
                return mid + 1
            else:   
                # 
                return mid 
    
if __name__ == "__main__":
    sol = Solution()
    tests = [ [[1, 3, 5],[2, 6, 9], [3, 6, 9]], [[5],[4],[3],[1],[3],[1],[4],[2],[5],[3],[3] ] ]

    print "answer is {0}".format(sol.findMedian(tests[1]))
    #print sol.binary_search(A[1], 8)
