

# largest continious black shape
# 0 = white
# 1 = black
# [[0, 0, 1, 0],
#  [0, 1, 1, 0],
#  [0, 1, 0, 1]]


# general overview

# how many ones do I see in each direction 
# add up sum from all directions

def maxNumberOnes(M,visited, r, c):
    #global visited
    # mark us visited
    visited[r][c] = 1
    
    #initialize 
    eastSean = 0
    southSean = 0
    westSean = 0
    northSean = 0
    
    # try go east make sure we don't go off east
    if c+1 < len(M[r]) and M[r][c+1] and not visited[r][c+1]:
        eastSean = maxNumberOnes(M, visited, r, c+1)
    
    # south
    if  r+1 < len(M) and M[r+1][c]  and not visited[r+1][c]:
        southSean = maxNumberOnes(M, visited, r+1, c)
        
    # west    
    if c-1 >= 0 and M[r][c-1] and not visited[r][c-1]:
        westSean = maxNumberOnes(M, visited, r, c-1)
         
        
    # north  
    if r-1 >= 0 and M[r-1][c] and not visited[r-1][c]:
        northSean = maxNumberOnes(M, visited, r-1, c)
    
    return 1 + eastSean + southSean + westSean + northSean





def main():
         
    visited = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]     
    M = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    
    maxSoFar = 0
    for r in range(0,len(M)):
        
        for c in range(0,len(M[r])):
            
            # make sure we start at 1 
            if M[r][c]:
                numberOfOnes = maxNumberOnes(M, visited, r, c)
                
                if numberOfOnes > maxSoFar:
                    maxSoFar = numberOfOnes
                       
    print maxSoFar
                
    



main()