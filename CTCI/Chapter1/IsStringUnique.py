__author__ = "Jonathan Mares"

# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

#Using Hashtable
def uniqueChars(str):
    chars = {}
    for x in str:
        try:
            if chars[x]==True:
                return False
        except:
            chars[x]=True
    return True

#Using No additional data structures,
# this is not efficient tho (n^2)
# because calls find on every element, which is itself O(n)
def uniqueChars2(str):
    for x in range (0,len(str)):
        if str[x] in str[x+1:]:
            return False
    return True
# better way, O(nlogn) time
def uniqueChars3(str):
    sorted_string = sorted(str)
    for x in range(0,len(sorted_string)-1):
        if sorted_string[x] == sorted_string[x+1]:
            return False
    return True




testStrings =["Hello","Hhello","PPPP","aeoiu","abcdefghijklmnop"]
testBool =[False,False,False,True,True]

# returns true if all inputs are correct. Change to uniqueChars2 to test it.
def tester(strings,boolList):
    boolgen = []
    for str in strings:
        boolgen.append(uniqueChars3(str))
    if boolList == boolgen:
        return True
    else: return False
def main():
    print(tester(testStrings,testBool))

main()
