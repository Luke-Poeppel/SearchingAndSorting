class ArrayDeque:
	'''
	Implementation of the Deque ADT.

	>>> d = ArrayDeque()
	>>> d.enqueue_first(1)
	>>> d.enqueue_last(2)
	>>> d.enqueue_first(3)
	>>> print(d.data)
	[1, 2, 3]
	'''
	INITIAL_CAPACITY = 3

	def __init__(self):
		self.data = [None] * ArrayDeque.INITIAL_CAPACITY
		self.num_of_elems = 0
		self.front_index = None
		self.back_index = None

	def __len__(self):
		return self.num_of_elems

	def is_empty(self):
		return (self.num_of_elems == 0)

	def enqueue_first(self, elem):
		if self.num_of_elems == len(self.data):
			self.resize(2 * len(self.data))

		if self.is_empty():
			self.data[0] = elem
			self.front_index = 0
			self.back_index = 0
			self.num_of_elems = 1
		else:
			self.front_index = (self.front_index - 1) % len(self.data)
			self.data[self.front_index] = elem
			self.num_of_elems += 1

	def enqueue_last(self, elem):
		if self.num_of_elems == len(self.data):
			self.resize(2 * len(self.data))

		if self.is_empty():
			self.data[0] = elem
			self.front_index = 0
			self.back_index = 0
			self.num_of_elems = 1
		else:
			self.back_index = (self.back_index + 1) % len(self.data)
			self.data[self.back_index] = elem
			self.num_of_elems += 1

	def dequeue_first(self):
		if self.is_empty():
			raise Exception("Queue is empty.")

		value = self.data[self.front_index]
		self.data[self.front_index] = None
		self.front_index = (self.front_index + 1) % len(self.data)
		self.num_of_elems -= 1

		if self.is_empty():
			self.front_index = None
			self.back_index = None
		elif self.num_of_elems < (len(self.data) // 4):
			self.resize(len(self.data) // 2)

		return value

	def dequeue_last(self):
		if self.is_empty():
			raise Exception("Queue is empty.")

		value = self.data[self.back_index]
		self.data[self.back_index] = None
		self.back_index = (self.back_index - 1) % len(self.data)
		self.num_of_elems -= 1

		if self.is_empty():
			self.front_index = None
			self.back_index = None
		elif self.num_of_elems < (len(self.data) // 4):
			self.resize(len(self.data) // 2)

		return value

	def first(self):
		if self.is_empty():
			raise Exception("Queue is empty.")
		else:
			return self.data[self.front_index]

	def last(self):
		if self.is_empty():
			raise Exception("Queue is empty.")
		else:
			return self.data[self.back_index]

	def resize(self, new_cap):
		old_data = self.data
		new_data = [None * new_cap]
		old_index = self.front_index

		for new_index in range(self.num_of_elems):
			new_data[new_index] = old_data[old_index]
			old_index = (old_index + 1) % len(old_data)

		self.data = new_data
		self.front_index = 0
		self.back_index = self.front_index + self.num_of_elems - 1

if __name__ == "__main__":
	import doctest
	doctest.testmod()