
dict = {"GO":True,"L":True, "POLE":True, "SOAP":True, "RELOG":True, "GOAL":True, "GERELGA":True}
foundWords = []

def findAllWords():
    for x in range(0,1):
        for y in range(0,1):
            visitedCoords = [[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]
            wordSearch((x,y),[],visitedCoords)

# Helpers

def wordSearch((x,y),wordSoFar,visitedCoords):
    # mark that we visited that coordinate
    visitedCoords[x][y] = True
    
    # if the word so far exists in our dictionary, add it to our 
    # found words
    
    # convert list to string
    wordSoFarString = ''.join(wordSoFar)
    try:
        if dict[wordSoFarString]:
            foundWords.append(wordSoFarString)
            #print wordSoFarString
    except:
        pass
    
    # main loop
    for xa in range(-1,2):
        for ya in range(-1,2):
            newCoord = (x+xa,y+ya)
            if isValid(newCoord,visitedCoords):
                print newCoord
                wordSoFar.append(G((x,y)))
                print(wordSoFar)
                print visitedCoords
                print "\n"
                wordSearch(newCoord, wordSoFar,visitedCoords)
    

# see if the coordinate given is a valid coordinate based on our system
def isValid((x,y),visitedCoords):
    xValid = x>=0 and x<4
    yValid = y>=0 and y<4
    return xValid and yValid and not visitedCoords[x][y]




# map english to code stuff 
def G((x,y)):
    G = [['A','D','E','G'],['F','G','E','O'],['P','O','L','R'],['S','A','E','R']]
    return G[x][y]


def main():
    findAllWords()
    print foundWords
    
main()