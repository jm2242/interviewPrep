class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        sub_list_len = len(A[0])
        print [m[sub_list_len/2] for m in A]


def main():
	sol = Solution()
	test = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
	sol.findMedian(test)


if __name__ == "__main__":
    main()