from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        
        if k > len(nums):
            return max(nums)

        # Linear solution
        d = deque()
        maxNums = []

        # the left most index of the current window
        leftBound = 0

        # First step: fill up to k
        for i in range(k):
            if d:
                
                # check all indeces in the deque
                for j in reversed(list(d)):
                    if nums[j] < nums[i]:
                        d.pop()
            
            d.append(i)
            
            # add element to deque
         
        for i in range(k,len(nums)):

            # add max element to our max number list
            maxNums.append(nums[d[0]])
            leftBound += 1

            # check all front elements
            for j in list(d):
                if j < leftBound:
                    d.popleft()

            # check all rear elements
            for j in reversed(list(d)):
                if nums[j] < nums[i]:
                    d.pop()

            d.append(i)

        # get the max of last window
        maxNums.append(nums[d[0]])ˇ
        return maxNums


    
        
        
        
        # Slower, O(nk) solution solution: 
        # window = []
        # length = len(nums)
        # for rbound in range(k-1,length):
        #     lbound = rbound+1 - k
        #     window.append(max(nums[lbound:rbound+1]))
        # return window
            

if __name__ == "__main__":
    solution = Solution()
    test = [9,6,11,8,10,5, 4, 13, 93, 14] # [11, 11, 11,10,13,93]

    print solution.maxSlidingWindow(test, 4)




