def test_normal():
	return 2 + 2

def test_weird():
	return 2 
	+ 2

def test_proper():
	return 2 \
	+ 2


print test_normal()
print test_weird()
print test_proper()