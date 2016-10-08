__author__ = 'jonathanmares'

#return a compressed string, O(n) time O(n) space
def compress_string(string):
    new_string = []
    letter = string[0]
    count = 1
    compressible = False
    for x in range(1,len(string)):
        print("looking at char :", string[x])
        if string[x] == letter:
            print("increment on char:", string[x])
            count +=1
            if not compressible:
                compressible = True
        else:
            new_string.append(letter)
            new_string.append(str(count))
            letter = string[x]
            count = 1
        if x==len(string) - 1:
            new_string.append(letter)
            new_string.append(str(count))

    if compressible:
        return ''.join(new_string)
    else:
        return string



def main():
    str =  "helo"
    print(compress_string(str))


main()
