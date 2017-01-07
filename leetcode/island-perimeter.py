from Queue import Queue
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
            
        perim = 0
        
        # let's find a place to start our search, find any land tile
        start = self.getStart(grid)
        if start is None:
            return 0
        print "start is {0}".format(start)
        q = Queue()
        visited = {}
        
        # put starting coordinate in queue
        q.put(start)
        visited[start] = True
        
        while not q.empty():
            
            curr = q.get()
            print "visiting {0}".format(curr)
            
            # get curr's neighbors
            neighbors = self.getNeighbors(curr,grid)
            print "neighbors are: {0}".format(neighbors)
            # put neighbors in queue
            for neigh in neighbors:
                row,col = neigh
                if grid[row][col] and neigh not in visited:
                    print "adding {0}".format(neigh)
                    q.put(neigh)
                    # mark visited
                    visited[neigh] = True
            
            # calculate perimeter wrt inner tiles
            perim += self.calcPerim(neighbors, grid)

            # calculate perimeter due to border of map 
            # max contribution: 2 units
            row, col = curr
            perim += self.checkBorders(curr, grid)

            
            print visited

            print "current perimeter {0}".format(perim)
            
        return perim

    # if coord borders the ends of the map, need to add those segments
    def checkBorders(self, coord, grid):
        row, col = coord
        perim = 0

        if row == 0:
            perim += 1

        if row == len(grid)-1:
            perim += 1

        if col == 0:
            perim += 1

        if col == len(grid[0])-1:
            perim += 1
        return perim


    def f(self,accum, neigh, grid):
        if not grid[neigh[0]][neigh[1]]:
            return accum + 1
        else:
            return accum  
            
    # calculate the local perimeter
    def calcPerim(self, neighbors, grid):
        accum = 0
        for neigh in neighbors:
            accum = self.f(accum,neigh,grid)
        print "perimeter: {0}".format(accum)
        return accum


    def getNeighbors(self, coord, grid):
        
        row, col = coord
         # north
        neighbors = []
        if row > 0: 
            neighbors.append((row-1,col))
       
        # west
        if col > 0:
            neighbors.append((row,col - 1))
            
        # east
        if col < (len(grid[0]) - 1):
            neighbors.append((row,col + 1))
   
        # south
        if row < (len(grid) - 1):
            neighbors.append((row + 1,col))
        
        return neighbors
        
            
        
    
    def getStart(self, grid):
        for idr, row in enumerate(grid):
            for idc, col in enumerate(row):
                if grid[idr][idc]:
                    return (idr,idc)

        # if no land
        else:
            return None

if __name__ == "__main__":
    sol = Solution()
    tests = [ [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]], [[1,1],[1,1]] ] 
    print sol.islandPerimeter(tests[1])
