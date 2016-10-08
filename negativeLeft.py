






def negativesLeft(lst):
	for n in range(0,len(lst)):
		if lst[n] >= 0:
			continue
		else:
			# try moving right
			for x in range(0,n):
				if lst[x] >=0:
					lst[x], lst[n] = lst[n], lst[x]
				else:
					continue


	return lst

def main():
	test = [-8,1,3,-9,-2,10]
	print negativesLeft(test)


main()