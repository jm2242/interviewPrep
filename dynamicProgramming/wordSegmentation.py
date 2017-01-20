__author__ = 'jonathanmares'

import os

# using recursive backtracing
def wordSegmentation(wordDict, word):
    memoTable = {}
    return wordSegment(wordDict, word, memoTable)

def wordSegment(wordDict, word, memoTable):
    if word in wordDict:
        return word

    if word in memoTable:
        return memoTable[word]

    for idc, _ in enumerate(word):
        if word[:idc+1] in wordDict:
            suffixResult = wordSegment(wordDict, word[idc+1:], memoTable)
            if suffixResult is not None:
                return word[:idc+1] + " " + suffixResult

    memoTable[word] = None
    print memoTable
    return None


# original implementation using a stack
# too slow
def wordSegmentationSlow(wordDict,word):
    
    segmentedWords = []
    segmentedEnds = []
    c = 0
    subWord = ''

    wordDict = dict(zip(wordDict,len(wordDict)*[True]))
    while c < len(word):
        #print segmentedWords
        # append current character to subWord
        subWord += word[c]

        if subWord in wordDict:
            segmentedWords.append(subWord)
            segmentedEnds.append(c)
            subWord = ''

        c += 1

        # if we get to the end the word and subWord is not empty, 
        # we need to backtrack
        if c == len(word) and subWord:

            # if we have not segmented words by this point, then it is 
            # not possible to to segment the string
            if not segmentedWords:
                break

            # otherwise try to extend the previous word
            else:

                # get the previous subWord and the index where it ended
                subWord = segmentedWords.pop()
                c = segmentedEnds.pop()

                # advance c by 1 as not to repeat the subWord
                c += 1


        

    return segmentedWords


if __name__ == "__main__":
    wordDict= {"app", "apple","pie","hole","section","solid"}
    print wordSegmentation(wordDict, "applepie") 
    print wordSegmentation(wordDict, "apple")
    
    
    longString = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordList = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    wordDict = dict(zip(wordList,len(wordList)*[True]))
    print wordSegmentation(wordDict, longString)

