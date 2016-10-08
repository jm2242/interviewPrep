__author__ = 'jonathanmares'


def isAnagram(word1,word2):
    if len(word1) != len(word2):
        return False
    word1_letter_counts = {}
    word1 = word1.lower()
    word2 = word2.lower()
    # count the number of letters in word1
    for c in word1:
        try:
            word1_letter_counts[c] += 1
        except KeyError:
            word1_letter_counts[c] = 1
    print(word1_letter_counts)

    # now see if each letter in word2 appears in word1 the exact number of times
    # subtract from word1_letter_counts, if every key is 0, then word is anagram
    for c in word2:
        if c not in word1_letter_counts:
            print (c,"is not in the dict")
            return False
        else:
            word1_letter_counts[c] -= 1

    for key in word1_letter_counts:
        if word1_letter_counts[key] != 0:
            return False

    return True


def main():
    word1 = "hellohi"
    word2 = "helolhi"
    print(isAnagram(word1,word2))

main()
