



def diffWord(word,subWord):
	shorterWord = word
	for m in re.finditer(subWord, word):
		print m.start()
		shorterWord = shorterWord[:m.start()] + shorterWord[m.end():]
	return shorterWord

def main():
	print diffWord("catdogcat","cat")

if __name__ == "__main__":
    main()