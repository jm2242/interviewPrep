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
                    
                    # only update the table at idx if a subsequence ending at idy can result
                    # in a longer subsequence at idx
                    if table[idx] <= table[idy]:
                        table[idx] += 1
       
            # check if max so far
            longestSubSeq = max(longestSubSeq, table[idx])
        return longestSubSeq

    # another way based on video, similar concept but more concise
    # def longestIncreasingSubsequence(self, nums):

    #     # define a list ls which is the length of the longest increasing subsequence
    #     # which includes element nums[i] as last element
    #     ls = len(nums) * [1]

    #     for idx, num in enumerate(nums):

            # need to find the max (ls[j]) such that j < i and nums[i] > nums[j]


                        
                
    