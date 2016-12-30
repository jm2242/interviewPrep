class Solution(object):
    # create a graph and keep track of state

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        self.graph = SimpleGraph(numCourses, prerequisites)
        
        # dictionary to store nodes already explored
        self.explored = {}

        # ordering variable
        #self.current_label = self.graph.nodeCount()

        # list to store topological sorting
        self.top_sort = []
        self.cycle = False
        
        self.dfs_loop()
        if not self.cycle:
            return self.top_sort
        else:
            return []
        
    def dfs_loop(self):

        # for every node 
        for node in self.graph.edges:
            
            # cycle detection
            if node in self.explored and node not in self.top_sort:
                self.cycle=True
            
            if node not in self.explored:
                self.explored[node] = True
                self.dfs(node)

        print self.top_sort
        


    def dfs(self, node):
        for to_node in self.graph.edges[node]:
            
            # cycle detection
            if to_node in self.explored and to_node not in self.top_sort:
                self.cycle = True
            
            if to_node not in self.explored:
                self.explored[to_node] = True
                self.dfs(to_node)

        #once we've exhausted all of the edges, we can add to topological sort
        self.top_sort.append(node)



class SimpleGraph:
    def __init__(self, numCourses, edges):
        self.edges = {}
        self.build_graph(numCourses, edges)

    def __str__(self):
        return str(self.edges)

    # build the graph from the supplied edges
    def build_graph(self, numCourses, edges):
        for edge in edges:
            node = edge[0]
            to_node = edge[1]
            if node in self.edges:
                self.edges[node].append(to_node)
            else:
                self.edges[node] = [to_node]

            # add the to_node to the edges dictionary with an empty list of edges,
            # if it doesn't exist yet
            if to_node not in self.edges:
                self.edges[to_node] = []
        '''
        due to odd leetcode graph input, we need to go through
        and make sure that for each integer from 0 to numCourses-1
        there is a a node in the graph to represent it
        '''
        for node in range(numCourses):
            if node not in self.edges:
                self.edges[node] = []
                
                
                
                
                
                