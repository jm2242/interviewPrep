class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = range(1,n+1)
        return self.worker(nums, k)


    def worker(self,nums, k):
        # base case
        if k ==0 or not nums:
            return []
        combs = []
        for idx, x in enumerate(nums[:len(nums)-k+1]):
            print "nums: {0}".format(nums)
            print "itteration: {0}".format(x)
            res = self.prependToAll( x, self.worker(nums[idx+1:],k-1) )
            print "merge result is: {0}".format(res)

            # append results to combinations so far
            combs +=res

        return combs

    def prependToAll(self, val, numList):
        print "val: {0}".format(val)
        print "numList {0}".format(numList)
        if not numList:
            return [[val]]
        f = lambda x, y=[val] : y+x
        return map(f,numList)

if __name__ == "__main__":
    sol = Solution()

    print sol.combine(5,3)