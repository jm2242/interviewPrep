# Python COnstructs
## `type`
- of course we an use `type()` to determine the type of of an object, since everything in python is an object, even types
- If we do something like this:

~~~ python
class Foo(object):
	pass
	
type(Foo)
<class 'type'>
~~~


- `type` is the type of all types, including itself
- `type` is a metaclass, or a "thing that builds classes"
- You can define metaclasses by setting a class's `__metaclass__` attribute to the metaclass you nuily


### Another, darker use of `type`
- we can create a new type with `type(name, bases, dict)`
- for example, we can create the Foo class above with `Foo = type('Foo', (), {})`
	- we can set member functions like so:

~~~ python 
def always_false(self):
	return False

Foo.always_false = always_false	
~~~ 
or, in one go: `Foo = type('Foo', (), {'always_false': always_false})`

and we can create classes that are dervied from other classes like so:
`Foo = type('FooBar, (Foo), {})`

### Is this useful?
- not so often apparnetly. 



## `eval`

Evaluate python code

## `__new__` vs `__init__`

- [Source](http://stackoverflow.com/questions/674304/pythons-use-of-new-and-init)
- Use `__new__` when you need to control the creation of a new instance. It's the first step of instance creation. called first, and is repsonsible for returning a new instance of your class. 
- In contrast, `__init__` doesn't return anything, it just initializes the instance after its been created

# Python Workings

## Objects
All objects have:

- unique identity, an integer returned by `id(x)`
- a type, as returned by `type(x)`
- some content

Objects may zero or more methods or names

## Python - call by reference or value?
Neither. Call by object, or call by object reference