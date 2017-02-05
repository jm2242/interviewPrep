

# requires a list of coordinates, where each coordinate is a dictionary of x,y,z coordinates
def drone(route):
	zCoords = []
	for coord in route:
		zCoords.append(coord['z'])

	current = zCoords[0]
	fuel = 0
	min_fuel = 0
	for pos in zCoords[1:]:
		fuel += current - pos
		current = pos
		min_fuel = min(min_fuel, fuel)

	return min_fuel

if __name__ == "__main__":
	route = [{'x':0, 'y':2, 'z':10}, {'x':3, 'y':5, 'z':0}, {'x':9, 'y':20, 'z':6}, {'x':10, 'y':12, 'z':15}, {'x':10, 'y':10, 'z':8}] 
	print drone(route)

