import collections
import heapq
from implementation import *

# Requires Python 3
# this is not my code
# I have taken this from Red Blob Games -> amazing resource

# basic queue wrapper for deque
class Queue:
	def __init__(self):
		self.elements = collections.deque()

	def empty(self):
		return len(self.elements) == 0

	def put(self, x):
		self.elements.append(x)

	def get(self):
		return self.elements.popleft()

class PriorityQueue:
	def __init__(self):
		self.elements = []

	def empty(self):
		return len(self.elements) == 0

	def put(self, item, priority):
		heapq.heappush(self.elements, (priority, item))


	def get(self):
		return heapq.heappop(self.elements)[1] # get data of tuple
 
def dijkstra_search(graph, start, goal):
	frontier = PriorityQueue()
	frontier.put(start, 0)
	came_from = {}
	cost_so_far = {}
	came_from[start] = None
	cost_so_far[start] = 0

	while not frontier.empty():
		current = frontier.get()

		if current == goal:
			break

		for next in graph.neighbors(current):
			new_cost = cost_so_far[current] + graph.cost(current, next)
			if next not in cost_so_far or new_cost < cost_so_far[next]:
				cost_so_far[next] = new_cost
				priority = new_cost
				frontier.put(next, priority)
				came_from[next] = current		


	return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
	current = goal
	path = [current]
	while current != start:
		current = came_from[current]
		path.append(current)

	path.append(start)
	path.reverse()
	return path





class SimpleGraph:
	def __init__(self):
		self.edges = {}

	def neighbors(self, id):
		return self.edges[id]

class GridWithWeights(SquareGrid):
	def __init__(self, width, height):
		super().__init__(width, height)
		self.weights = {}

	def cost(self, from_node, to_node):
		return self.weights.get(to_node, 1)





class SquareGrid:
	def __init__(self, width, height):
		self.width = width
		self.height = width
		self.walls = []

	def in_bounds(self, id):
		(x, y) = id
		return 0 <= x < self.width and 0 <= y < self.height

	def passable(self, id):
		return id not in self.walls

	def neighbors(self, id):
		(x, y) = id
		results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
		if (x+y) % 2 == 0: results.reverse()

		# make sure to only return in bounds neighbors
		results = filter(self.in_bounds, results)

		# make sure to only return neighbors which are passable
		results = filter(self.passable, results)
		return results




def breadth_first_search_1(graph, start):
	frontier= Queue()
	frontier.put(start)
	visited = {}
	visited[start] = True

	# while the queue isn't empty
	while not frontier.empty():
		# get next item from queue
		current = frontier.get()
		print("visiting {0}".format(current))

		# itterate over all the neighbors
		for next in graph.neighbors(current):
			if next not in visited:
				frontier.put(next)
				visited[next] = True

def breadth_first_search_2(graph, start):
	frontier= Queue()
	frontier.put(start)
	came_from = {}
	came_from[start] = None

	while not frontier.empty():
		current = frontier.get()
		for next in graph.neighbors(current):
		    if next not in came_from:
		        frontier.put(next)
		        came_from[next] = current

	return came_from

def breadth_first_search_3(graph, start, goal):
	frontier= Queue()
	frontier.put(start)
	came_from = {}
	came_from[start] = None

	while not frontier.empty():
		current = frontier.get()

		# if we reached our destination
		if current == goal:
			break

		for next in graph.neighbors(current):
		    if next not in came_from:
		        frontier.put(next)
		        came_from[next] = current

	return came_from

def heuristic(a,b):
	(x1, y1) = a
	(x2, y2) = b
	return abs(x1 - x2) + abs(y1 - y2)


def a_star_search_j(graph, start, goal):
	frontier = PriorityQueue()
	frontier.put(start, 0)
	came_from = {}
	cost_so_far = {}
	came_from[start] = None
	cost_so_far[start] = 0

	while not frontier.empty():
		current = frontier.get()

		if current == goal:
			break

		for next in graph.neighbors(current):
			new_cost = cost_so_far[current] + graph.cost(current, next)

			# if next hasn't been visited or the cost to visit this node is now lower
			if next not in cost_so_far or new_cost < cost_so_far[next]:
				cost_so_far[next] = new_cost

				# choose a priority 
				priority = new_cost + heuristic(goal, next)
				frontier.put(next, priority)
				came_from[next] = current

	return came_from, cost_so_far






if __name__ == '__main__':

	# Simple BFS
	graph = SimpleGraph()
	graph.edges = {
		'A': ['B'],
	    'B': ['A', 'C', 'D'],
	    'C': ['A'],
	    'D': ['E', 'A'],
	    'E': ['B']
	}
	#breadth_first_search_1(graph, 'A')

	# square grid
	g = SquareGrid(30,15)
	g.walls = DIAGRAM1_WALLS
	#parents = breadth_first_search_2(g, (8,7))
	parents = breadth_first_search_3(g, (8,7), (17,2))

	#draw_grid(g, width=2, point_to=parents, start=(8,7), goal=(17,2))
	# came_from, cost_so_far = dijkstra_search(diagram4, (1,4),(7,8))
	# draw_grid(diagram4, width=3, point_to=came_from, start=(1, 4), goal=(7, 8))
	# print()
	# draw_grid(diagram4, width=3, number=cost_so_far, start=(1, 4), goal=(7, 8))
	# print()
	# draw_grid(diagram4, width=3, path=reconstruct_path(came_from, start=(1, 4), goal=(7, 8)))
	came_from, cost_so_far = a_star_search_j(diagram4, (1, 4), (7, 8))
	draw_grid(diagram4, width=3, point_to=came_from, start=(1, 4), goal=(7, 8))
	print()
	draw_grid(diagram4, width=3, number=cost_so_far, start=(1, 4), goal=(7, 8))












