__author__ = 'jonathanmares'

#Question 1.3 From Arrays and String section
#N^2 implementation
def stringPermutation(str1, str2):
    #check if the strings have the same length
    if len(str1) != len(str2):
        return False
    for x in str1:
        if x not in str2:
            return False
    return True
print(stringPermutation("aaba","aaac"))



def genPermutation(str):
    return

######################

#Question 1.4 from Arrays and Strings section

# def spaceReplace(str):
#     space = []
#     for x in str:
#         if x==" ":
#
#
#
# spaceReplace("Hello ")
#















def listGen(lst):
    newList = []
    for x in range(0,len(lst)):
        newList.append(lst)
    return newList


def multFunc(lst):
    intermList = listGen(lst)
    finalList = []
    temp = 1
    for x in range(0,len(intermList)):
        print(x)
        for y in range(0,len(intermList[x])):
            print(y)
            if x==y:
                pass
            else:
                temp = temp * intermList[x][y]
        finalList.append(temp)
        temp = 1
    return finalList

#testList = [1,2,3,4]
#print(multFunc(testList))