import unittest
'''
requires a sorted list nums. If duplicate keys, returns one of the indexes (no guarantee which one)
finds if elem is in nums
returns the index of nums where elem exists, if it exists
otherwise, returns None
Runtime: if length is supplied O(logn), 

'''
def binary_search(nums, elem, length=None):
	low = 0
	high = length

	if length is None:
		length = len(nums)
		high = length - 1



	# exit loop when low is either high or greater, depending on if odd or even
	# number of elements
	while low <= high:
		# get the middle 
		mid = low + (high - low) / 2
		if nums[mid] == elem:
			return mid
		elif nums[mid] > elem:
			high = mid - 1
		elif nums[mid] < elem:
			low = mid + 1

	else:
		return None
 


def main():
	tests = [[0,1,2,3,4,5,6], [4,5,6,7,8,9],[-100,2,4,4,8,10,100]]
	for x in range(7):
		ans = binary_search(tests[0],x)
		assert ans  == x

	assert binary_search(tests[1],9) == 5
	assert binary_search(tests[1],6) == 2
	assert binary_search(tests[0],10) == None
	assert binary_search(tests[2],-100) == 0
	assert binary_search(tests[2],4) == 3










if __name__ == "__main__":
	main()