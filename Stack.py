class ArrayStack(object):
	'''
	Implementation of the Stack ADT.
	
	>>> s = ArrayStack()
	>>> for i in range(1, 4):
	...     s.push(i)
	>>> s.data
	[1, 2, 3]
	>>> s.top()
	3
	>>> s.pop()
	3
	>>> s.pop()
	2
	>>> s.top()
	1
	>>> len(s)
	1
	'''
	def __init__(self):
		self.data = []

	def __len__(self):
		return len(self.data)

	def is_empty(self):
		return (len(self.data) == 0)

	def push(self, item):
		self.data.append(item)

	def pop(self):
		if (self.is_empty() == True):
			raise Exception("Stack is empty!")
		else:
			return self.data.pop()

	def top(self):
		if (self.is_empty() == True):
			raise Exception("Stack is empty!")
		else:
			return self.data[-1]

if __name__ == "__main__":
	import doctest
	doctest.testmod()