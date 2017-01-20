from collections import defaultdict
# Complete the function below.

def  krakenCount(m, n):
    
    # store cells we have visited already
    visited = defaultdict(lambda: False)
    return explore(0,0, visited, m-1, n-1)
    

def explore(r, c, visited, m, n):
    print visited
    # if we reached the goal
    if (r,c) == (m,n):
        return 1
    numberOfWays = 0
    for neighbor in getNeighbors(r,c, m, n):
        
        if not visited[neighbor]:
            r2, c2 = neighbor
            numberOfWays += explore(r2, c2, visited, m, n)
            
        # otherwise we visited this node, check visited dictionary
        else:
            numberOfWays += visited[neighbor]
        
    # mark that we visited this coordinate by marking the number of ways
    # we can get to the goal state from this node
    visited[(r, c)] = numberOfWays
    
    return numberOfWays
    
    
    
# return the neighbors that are reachable from coordinate r, c
# requires the coordinates r,c and the size of the map m, n
def getNeighbors(r, c, m, n):
    neighbors = []
    
    # if we aren't at the last row of the map
    if r < m:
        neighbors.append((r+1, c))
        
    # if we aren't at the last column of the map
    if c < n:
        neighbors.append((r, c+1))
        
    # can only go diagonal if not at last row and last column
    if r < m and c < n:
        neighbors.append( (r+1, c+1) )
    
    return neighbors
    
        
if __name__ == "__main__":
    print krakenCount(2,2)

