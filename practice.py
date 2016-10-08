__author__ = 'jonathanmares'


string = 'hello'

#returns True if all the characters in the string are unique. False otherwise. Returns true for empty string
#requires a string
#returns a boolean
def uniqueChars(str):
    chars = {}
    for x in str:
        try:
            if chars[x]==True:
                return False
        except:
            chars[x]=True
    return True

#find the permutations of a string. Recursively finds all possibilitites
#requires a string
#returns a list of permutations
def permutations(str):
    if len(str) == 0:
        raise "len is 0"
    elif len(str) == 1:
        #print(str)
        return [str]
    else:
        temp = []
        for index,x in enumerate(str):
            #print("Removing this character: ", x)
            toList = list(str)
            toList[index] = ""
            string_with_character_removed = ''.join(toList)
            #print("figuring out how to combine ", x, " with ", string_with_character_removed)
            ways = [x + sub for sub in permutations(string_with_character_removed)]
            #print("The ways are: ", ways)
            temp +=ways
    return set(temp)

#the way interviewcake does it. Use the last character is the "pop" off characgter, attaching it to all
#permutations of the rest of the characters
def get_permutations(string):
    #base case
    if len(string) <= 1:
        return [string]

    all_except_last = string[:-1]
    last_char = string[-1]

    #get the permutations of all except last
    permutations_all_except_last = get_permutations(all_except_last)

    #combine the last character with all of the permutations
    permutations = []
    for x in range(0,len(permutations_all_except_last)):
        for pos in range(0,len(permutations_all_except_last[x])+1):
            permutations.append(permutations_all_except_last[x][:pos] + last_char +
            permutations_all_except_last[x][pos:])

    return permutations

def main():
    print(permutations("123"))
    print(get_permutations("123"))

main()