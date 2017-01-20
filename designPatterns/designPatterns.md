# Design Patterns

## Overview
1. Creational
2. Structural
3. Behavioral

# Creational Patterns


## Singleton 

### Intentions
- Ensure one object gets created
- provide global access point
- controll concurrent access to resources that are shared


### Use Cases
- logging or database operations
- thread pools, caches, dialogue boxes
- registry settings
- printer spoolers

### Implementation

~~~ python
class Singleton(object):
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Singleton, cls).__new__(cls)
		return cls.instance

------
s = Singleton()

s1 = Singleton()	
~~~

- `__new__` is Python's special method to instantiate object
	- 	we override to control the object creation
	-  basically prevent another object of that class to be instantiated


### Lazy instantiation
- work with reduced resources and create them only when needed



~~~ python
class Singleton:
	__instance = None
	def __init__(self):
	if not Singleton.__instance:
		print("__init__ method called")
		
	else:
		print("Instance already created:", self.getInstance())
	
	@classmethod
	def getInstance(cls):
		if not cls.__instance:
			cls.__instance = Singleton()
		return cls.__instance
		
	
	s = Singleton() # class initialized, but object not created
	print("object created", Singleton.getInstance())
	
	s1 = Singleton() # instance already created

~~~
### Module level singletons
- all modules are singletons by default because of Python importing behavior
- How does python work?
	1.  check whether a Python module has been imported 
	2. if imported, returns object for module, if not imported, instantiate it
	3. when module gets imported, it is intiialized. does not get initialized if it is imported again

### Monostate Singleton Pattern
- What does a programmer need? instances sharing the same state
- Let's try this:

~~~ python
class Borg:	
	__shared_state = {"1":"2"}
	def __init__(self):
		self.x = 1
		self.__dict__ = self.__shared_state
		pass
		
		
----
# Now lets make the objects
b = Borg()
b1 = Borg()
b.x = 4

# b and b1 are distinct objects, but b and b1 share the same state:
print("b state", b.__dict__)
print("object state b1", b1.__dict__)	
~~~
Output of shared state Borg

![Output](./borgOutput.png "Ouput")

- `__dict__` variable assigned to `__shared_state`
	- `__dict__` is used to store state of every object of a class
	- we intentionally assigned `__shared_state` to all created instance
- technically, we get two different objects unlike **Singleton**. But we share state
- We can also do it like this:

~~~ python
class Borg(object):
	_shared_state= {}
	def __new__(cls, *args, **kwargs):
		obj = super(Borg, cls).__new__(cls, *args, **kwargs)
		obj.__dict__ = cls._shared_state
		return obj
~~~
### Singletons and metaclasses
### What are metaclasses?
- metaclass is a class of a class, aka class is an innstane of its metaclasses
- you can create classes of your own type from predefined Python classes
- since `type(int)` returns `type`, we know there is a metaclass present
- What happens when create some `class A`?
	- Python creates it by ` A = type(name, bases, dict) `
	- `name` -> name of the class
	- `base` -> base class
	- ` dict ` -> attribute variable
- Python's special `__call__` method gets called when an object needs to be created for an already existing class

Let's implement Singleton with metaclasses:

``` python
class MetaSingleton(type):
	_instances = {}
	def __cal__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwrargs)
		return cls._instances[cls]
		
class Logger(metaclass=MetaSingleton):
	pass

logger1 = Logger()
logger2 = Logger()
	
```

### Practical Use Case 1 - database application
- Consider example of cloud service that involves read and write operations on database
- service is spread across multiple services
- action on UI of web app internally calls API which eventually results in a DB operation
- Shared resource across different resource is database itself
	- need to take care of consistency across operations in database, operations should result in conflicts 
	- memory and CPU utilization should be optimized for handling of multiple operations on databse	
#### Sample Python implementation

``` python
import sqlite

# create a metaclass
class MetaSingleton(type):
	_instances = {}
	
	# special __call__ method is used in the metaclass to create a Singleton
	def __cal__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwrargs)
		return cls._instances[cls]
	
# decorated by the MetaSingleton class	
class Database(metaclass=MetaSingleton):
	connection = None
	def connect(self):
		if self.connection is None:
			self.connection = sqlite3.connect('db.sqlite3')
			self.cursorobj = self.connection.cursor()
		return self.cursorobj
	
db1 = Database().connect()
db2 = Database().connect()

# these will print the same cursor object at the same memory location
print ("database boejcts DB1", db1)
print ("Databse object DB2", db2)
	
```
- When `Database` class is instantatiated, it creates only one object
- When application wants to make operations on DB, it gets access to 1 database object
	- calls are therefore synchronized, and inexpensive on system resources	
- What if we have a clustered setups with multiple web apps but only 1 DB?
	- hmm, not good for Singletons because every web app adds a Singleton and a database query object
	- will result in unsynchronized database operations and is heavy on resources
	- we should use database connection pooling rather than Singletons

### Practical Use Case 2 - Health Check Service 

#### Implementation

~~~ python
class HealthCheck:
	_instance = None
	def __new__(cls, *args, **kwargs):
		if not HealthChek._instance:
			HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
		return HealtCheck._instance
	
	def __init__(self):
		self._servers = []
	
	def addServer(self):
		self._servers.append("server 1")
		self._servers.append("server 2")
		self._servers.append("server 3")
	
	def changeServer(self):
		self._servers.pop()
		self._servers.append("Server 5")
		
hc1 = HealthCheck()
hc2 = HealthCheck()	
	

~~~ 	


### Drawbacks of Singleton Pattern
- Global variables can be changed by mistake at one place, and may be used incorrectly by developer in other places
- multiple references may get created to the same object
- tight coupling to global variables, since global data by one class can inadvertently impact other lasses


## Factory Design Pattern

### Overview
- arguably most used design pattern
- useful because it creates a simplified implementation for client, and adding new classes to factory don't need to be done by client, who doesn't need to know about these details



### Understanding
- factory -> class responsible for creating objects of other types
- typically, factory class has an object and methods associated with
- client class this methodwith certain parameters
- Why do we need a factory class if the client can directly create an object? Some advantages:
	- loose coupling, object can be created independent of class implementation
	- A simplified implemntation for the client. client doesn't need to know of class that creates the object
	- adding another class to factory to create objects of another type can be easily done without the client changing the code. Client can just pass another parameter


### Variants of Factory Pattern
- Simple Factory pattern
	- allows interfaces to create objects without exposing object creation logic
- Factory Method pattern
	- allows interfaces to create objects, but defers decision to subclasses to determine the class for object creation 
- Abstract Factory Pattern
	- abstract factory is an interface to create related objects without speicfying/exposing their classes
	- provides objects of another factory


#### Simple Factory Pattern


~~~ python

~~~ 




















- page extend
- page extend
- page extend
- page extend
- page extend
- page extend
- page extend
- page extend
- page extend
- page extend
- page extend
- page extend
- page extend
- page extend
- page extend
- page extend
- page extend
- page extend
- page extend
- page extend
- page extend
- page extend
- page extend
- page extend
















