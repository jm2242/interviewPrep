from abc import ABCMeta, abstractmethod

''' basic assumptions
-parking lot has many levels, each level has multiple rows of spots
-parking lot can park motorcycles, cars, and buses
-parking lot has motorcycle spots, compact spots, and large spots
-motorcycle can park in any spot
-car can park in either a single ompact spot or a single large spot

-a bus can park in five large spots that are consecutive and within the same row,
but cant park in small spots
'''


# singleton class
class ParkingGarage1(object):
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Singleton, cls).__new__(cls)
		return cls.instance

# or, we can do it the borg way:

class Borg:
	# all objects share this state
	_shared_state = {}
	def __init__(self):
		self.__dict__ = self._shared_state

class ParkingGarage2(Borg):
	def __init__(self):
		Borg.__init__(self)

# or:

class ParkingGarage3(object):
	# class attribute
	__instance = None
	def __new__(cls, levels=0, rows=0, motorcycleSpots, compactSpots, largeSpots):
		if ParkingGarage3.__instance is None:
			ParkingGarage3.__instance = object.__new__(cls)
		ParkingGarage3.__instance.levels = levels
		ParkingGarage3.__instance.rows = rows
		ParkingGarage3.__instance.vehicles = {}
		return ParkingGarage3.__instance
	
	def charge(self): 

	def isFull(self):

	def canPark(self):

	def vehicleEnter():


	def vehicleLeave():

	def __str__(self):
		string = "Parking Garage has {0} levels and {1} rows".format(self.levels, self.rows)
		return string
	

class Vehicle(metaclass=ABCMeta):
	VEHICLE_TYPES = ('MOTORCYCLE', 'CAR', 'BUS')
	SPOTS_NEEDED = (1, 1, 5)

	def __init__(self, vehicleType, licensePlate):
		self.vehicleType = vehicleType
		self.licensePlate = licensePlate



	@abstractmethod
	def vehicle_type():


	@abstractmethod
	def canFit(self):


class Bus(Vehicle):

	def canFit(self):
		






def main():
	garage = ParkingGarage3(5, 20)
	print garage



























if __name__ == "__main__":
	main()