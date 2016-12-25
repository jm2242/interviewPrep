class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # edge case
        if not nums:
            return 0
        
        # keep track of the longest sub sequence in the table
        longestSubSeq = 1
        
        # keep track of the longest subsequence up to each index i in nums
        table = len(nums) * [1]
        
        # itterate over all nums in i
        for idx, numx in enumerate(nums):
            
            # check all indeces up to idx
            for idy, numy in enumerate(nums[:idx]):
                
                # only interested in cases where numx, the number ahead in the list,
                # is larger than the number preceeding it
                if numx > numy:
                    
                    # only update the table at idx
                    if table[idx] <= table[idy]:
                        table[idx] += 1
       
            # check if max so far
            longestSubSeq = max(longestSubSeq, table[idx])
        return longestSubSeq
                        
                
        