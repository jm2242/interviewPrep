import heapq
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        graph = constructGraph(beginWord, endWord, wordList)
        return dijkstraSearch(graph, beginWord, endWord)
        
        


class PriorityQueue:
    def __init__(self):
        self.frontier = []
    def empty(self):
        return len(self.frontier) == 0
        
    def put(self, item, priority):
        heapq.heappush(self.frontier, (priority, item))
    
    # get the item with highest priority
    def get(self): 
        return heapq.heappop(self.frontier)[1]
 
def constructGraph(beginWord, endWord, wordList):
    graph = SimpleGraph()
    wordList = list(wordList)
    wordList.append(beginWord)
    wordList.append(endWord)

    for word in wordList:
        graph.edges[word] = []
        for y in wordList:
            
            # find all possible nodes that are neighbors
            # differByOne takes care of case where word and y are the same
            if differByOne(word, y):
                graph.edges[word].append(y)
    
    return graph
            
            
            
            
        
    
    return graph

# return True if words differ by exaclty one character
def differByOne(word1, word2):
    length = len(word1)
    difference = 0
    for x in range(length):
        if word1[x] != word2[x]:
            difference +=1
        
        # allow for early exit
        if difference > 1:
            return False
    else:
        if difference == 0:
            return False
        else: 
            return True



def dijkstraSearch(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 1)
    cost_so_far = {}
    
    # initialize start node
    cost_so_far[start] = 1
    
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                
    if goal in cost_so_far:
        return cost_so_far[goal]
    else:
        return 0
            



# Our graph
class SimpleGraph:
    def __init__(self):
        # dictionary of edge lists
        self.edges = {}
        
    def neighbors(self, id):
        return self.edges[id]
        
    
if __name__ == "__main__":
    solution = Solution()
    print solution.ladderLength("hit","cog",["hot","dot","dog","lot","log"])



