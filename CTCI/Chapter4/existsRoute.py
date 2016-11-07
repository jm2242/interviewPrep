import collections
import sys
# PROMPT
#Route Between Nodes: Given a directed graph, design an algorithm to  find 
#out whether there is a route between two nodes.


class SimpleGraph:
	def __init__(self):
		self.edges = {}

	def neighbors(self, id):
		return self.edges[id]

class Queue:
	def __init__(self):
		self.elements = collections.deque()

	def empty(self):
		return len(self.elements) == 0
	def push(self, node):
		self.elements.append(node)

	def pop(self):
		return self.elements.popleft()


# return True if there exists a way to get to goal node
# return False otherwise
def existsRoute(graph, start, goal):
	frontier = Queue()
	visited = {}

	frontier.push(start)

	# if start and goal are the same
	if start == goal:
		return True

	while not frontier.empty():
		# get element from queue
		current = frontier.pop()
		print "Currently Visiting {0}".format(current)



		# loop over all of the neighbors in next
		for next in graph.neighbors(current):

			# if we can get there, then we're good
			if next == goal:
				return True


			if next not in visited:
				visited[next] = True
				frontier.push(next)
	# if we never encountered the start node, then we should return false
	return False


def main():

	graph = SimpleGraph()
	graph.edges = {
	'A': ['B'],
	'B': ['A', 'C', 'D'],
	'C': ['A'],
	'D': ['E', 'A'],
	'E': ['B']
	}


	print existsRoute(graph, 'A', 'E')
	return 0




if __name__ == '__main__':
        sys.exit(main())













