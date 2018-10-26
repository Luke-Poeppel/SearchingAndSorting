class ArrayQueue(object):
	'''
	Implementation of the Queue ADT (FIFO).

	>>> q = ArrayQueue()
	>>> q.enqueue(10)
	>>> q.enqueue(11)
	>>> q.enqueue(12)
	>>> q.data
	[10, 11, 12]
	>>> q.dequeue()
	10
	>>> q.first()
	11
	>>> q.__len__()
	2
	'''
	INITIAL_CAPACITY = 3

	def __init__(self):
		self.data = [None] * ArrayQueue.INITIAL_CAPACITY
		self.num_of_elems = 0
		self.front_index = None

	def __len__(self):
		return self.num_of_elems

	def is_empty(self):
		return (len(self) == 0)

	def enqueue(self, elem):
		if self.num_of_elems == len(self.data):
			self.resize(2 * len(self.data))

		if self.is_empty():
			self.data[0] = elem
			self.front_index = 0
			self.num_of_elems += 1
		else:
			back_index = (self.front_index + self.num_of_elems) % len(self.data)
			self.data[back_index] = elem
			self.num_of_elems += 1

	def dequeue(self):
		if self.is_empty():
			raise Exception("Queue is empty.")

		val = self.data[self.front_index]
		self.data[self.front_index] = None
		self.front_index = (self.front_index + 1) % len(self.data)
		self.num_of_elems -= 1

		if self.is_empty():
			self.front_index = None
		elif (self.num_of_elems < len(self.data) // 4):
			self.resize(len(self.data) // 2)

		return val

	def first(self):
		if self.is_empty():
			raise Exception("Queue is empty!")

		return self.data[self.front_index]

	def resize(self, new_cap):
		old_data = self.data
		self.data = [None] * new_cap
		old_index = self.front_index

		for new_index in range(self.num_of_elems):
			self.data[new_index] = old_data[old_index]
			old.index = (old_index + 1) % len(old_data)

		self.front_index = 0

if __name__ == "__main__":
	import doctest
	doctest.testmod()