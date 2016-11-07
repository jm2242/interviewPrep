import collections

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        (rows, columns) = len(grid), len(grid[0])
        #essentially a helper object
        myGrid = SquareGrid(rows, columns, grid)
        islands = 0
        # now we need to try to start from every possible position in the grid
        # we'll check if we visited, and if so, then we can pass
        for r in range(rows):
            for c in range(columns):

                if not myGrid.haveVisited((r,c)) and myGrid.passable((r,c)):
                    islands += breadth_first_search(myGrid, (r,c))
                    print islands
        return islands 
        
        
def breadth_first_search(graph, start):
    frontier = Queue()
    frontier.put(start)
    graph.visited[start] = True

    while not frontier.empty():
        current = frontier.pop()

        
        
        for next in graph.neighbors(current):
            frontier.put(next)
            graph.visited[next] = True
    
    return 1
    


class Queue:
    def __init__(self):
        self.elements = collections.deque()
        
    def empty(self):
        return len(self.elements) == 0 
    
    def put(self, element):
        self.elements.append(element)
        
    def pop(self):
        return self.elements.popleft()


class SquareGrid:
    def __init__(self, rows, columns, grid):
        self.columns = columns
        self.rows = rows
        
        #2D list that is given to us by the problem
        self.grid = grid
        
        # a dictionary of coordinates that we have visited
        self.visited = {}
    
    # return True if the coordinate is 1, False otherwise
    def passable(self, coordinates):
        (r, c) = coordinates
        return int(self.grid[r][c]) == 1
        
    def haveVisited(self, coordinates):
        return coordinates in self.visited
    
    def haveNotVisited(self, coordinates):
        return coordinates not in self.visited

    def in_bounds(self, coordinates):
        (r, c) = coordinates
        
        return 0 <= r < self.rows and 0 <= c < self.columns
    
    def neighbors(self, coordinates):
        (r, c) = coordinates
        results = [(r+1,c),(r,c+1),(r,c-1),(r-1,c)]
        
        # make sure to only return in bounds neighbors
        results = filter(self.in_bounds, results)
        
        # make sure we can go there (a 1 at these locations
        results = filter(self.passable, results)

        results = filter(self.haveNotVisited, results)

        return results
        
        
if __name__ == "__main__":
    solution = Solution()
    solution.numIslands(["11000","11000","00100","00011"])
        
        
        
        
        
        