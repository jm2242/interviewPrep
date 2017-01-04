
'''
Implementation of Knuth-Morris-Pratt string matching. 
Run time: O(n+m) 

'''
class KmpMatching(object):
	"""
		Build the prefix table for pattern pat
        :type pat: str
        :rtype: List[int]
        """
	def prefix_table(self, pat):

		# table to store the longest prefix 
		table = [0] * len(pat)

		j = 0
		for i in range(1, len(pat)):

			# if characters don't match, increment i
			if pat[i] != pat[j]:
				
				# j reset while loop
				while j > 0 and pat[i] != pat[j]:

					# we now set j to be the value stored in table[j-1]
					# this part is kind of odd
					j = table[j-1]

					# if no match, continue to reassign j
					if pat[i] != pat[j]:
						continue

					# if match, increment j and break j reset loop
					else:
						table[i] = j + 1
						j += 1
						break

			else:
				# if characters match
				table[i] = j + 1
				j += 1

		return table
	'''
		find the index of the first occurence of pat in text
		return -1 if pat not in text
		:type pat: str
		:type text: str
        :rtype: int
		'''
	def search(self, pat, text):
		
		# prefix table
		table = self.prefix_table(pat)
		j = 0
		for i in range(len(text)):
			# if the pattern and text match
			if text[i] == pat[j]:

				# if we've reached the end of the pattern
				if j == len(pat) - 1:
					return i + 1 - len(pat)

				j += 1
				continue

			# if no match, then check value in j-1 index of table
			else:

				# change j only if it was somewhere in pattern
				while j > 0 and text[i] != pat[j]:
					j = table[j-1]
					if text[i] != pat[j]:
						continue
					else:
						j += 1
						break


		# no match
		return -1

def main():
	kmp = KmpMatching()
	text = "abxabcabcaby"
	pat = "abcaby"
	# tests = [{"text":"yoloyoloyoloyolo", "pat":"bob"}]
	# for test in tests:
	# 	text = test['text']
	# 	pat = test['pat']
	# 	assert kmp.search(pat, text) == -1
	# 	assert kmp.search("yolo", text) == 0
	print kmp.prefix_table("aacecaaa#aaacecaa")


if __name__ == "__main__":
    main()
        