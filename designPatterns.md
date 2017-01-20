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
	- 	we ovverride to control the object creation
