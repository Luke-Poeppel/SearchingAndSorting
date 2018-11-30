'''
Doubly linked list (ADT).
'''

class DoublyLinkedList(object):
	class Node(object):
		'''
		Data input (referrenced as the node below) can be of any format (or within
		any other data type.)
		'''
		def __init__(self, data = None, prev = None, next = None):
			self.data = data
			self.prev = prev
			self.next = next

		def disconnect(self):
			self.data = None
			self.prev = None
			self.next = None

	def __init__(self):
		'''
		Since the header and trailer nodes (or sentinels) are purely for position,
		they do hold data.
		'''
		self.header = DoublyLinkedList.Node()
		self.trailer = DoublyLinkedList.Node()
		self.header.next = self.trailer
		self.trailer.prev = self.header
		self.size = 0

	def __len__(self):
		return self.size

	def is_empty(self):
		return (len(self) == 0)

	#---------------------First and Last Data Nodes-----------------------
	def first_node(self):
		'''
		Returns the first node of a Doubly Linked List that holds data.
		'''
		if (self.is_empty()):
			raise Exception("List is empty!")
		else:
			return self.header.next

	def last_node(self):
		'''
		Returns the last node of a Doubly Linked List that holds data.
		'''
		if (self.is_empty()):
			raise Exception("List is empty!")
		else:
			return self.trailer.prev

	#---------------------Adding Data------------------------------------
	def add_after(self, node, data):
		'''
		Helper function for adding data to first and last locations.
		'''
		prev = node
		succ = node.next
		new_node = DoublyLinkedList.Node(data, prev, succ)
		prev.next = new_node
		succ.prev = new_node
		self.size += 1
		return new_node

	def add_first(self, data):
		return self.add_after(self.header, data)

	def add_last(self, data):
		return self.add_after(self.trailer.prev, data)

	def add_before(self, node, data):
		return self.add_after(node.prev, data)

	def insert_sorted(self, elem):
		if self.is_empty():
			self.first_node().data = elem
			self.size += 1
		
		if self.first_node().data >= elem:
			old_first = self.first_node()
			new_first = DoublyLinkedList.Node(elem, self.header, old_first)
			self.header.next = new_first
			old_first.prev = new_first
			self.size += 1
		elif self.last_node().data >= elem:
			old_last = self.last_node()
			new_last = DoublyLinkedList.Node(elem, old_last, self.trailer)
			self.trailer.prev = new_last
			old_last.next = new_last
			self.size += 1
		else:
			cursor = self.first_node().next
			while cursor is not self.trailer:
				if cursor.data >= elem:
					new_node = DoublyLinkedList.Node(elem, cursor.prev, cursor)
					cursor.prev.next = new_node
					cursor.prev = new_node
				else:
					cursor = cursor.next

			self.size += 1

		return

	#---------------------Deleting Data---------------------------------
	def delete_node(self, node):
		pred = node.prev
		succ = node.next
		pred.next = succ
		succ.prev = pred
		self.size -= 1
		data = node.data
		node.disconnect()
		return data

	def delete_first(self):
		if (self.is_empty()):
			raise Exception("List is empty!")
		return self.delete_node(self.first_node())

	def delete_last(self):
		if (self.is_empty()):
			raise Exception("List is empty!")
		return self.delete_node(self.last_node())

	#---------------------Traversal-------------------------------------
	def __iter__(self):
		if (self.is_empty()):
			return
		cursor = self.first_node()
		while cursor is not self.trailer:
			yield cursor.data
			cursor = cursor.next

	def __repr__(self):
		return "[" + " <--> ".join([str(item) for item in self]) + "]"

'''
lnk_lst1=DoublyLinkedList()
lnk_lst1.add_first(4)
lnk_lst1.add_first(2)
lnk_lst1.add_last(7)
lnk_lst1.add_last(3)
lnk_lst1.add_last([1,2,3])
print(lnk_lst1)

lnk_lst1.delete_first()
print(lnk_lst1)

lnk_lst2 = DoublyLinkedList()
lnk_lst2.add_first(13)
print(lnk_lst2.__len__())

lnk_lst2 = DoublyLinkedList()
lnk_lst2.add_first(2)
lnk_lst2.add_last(4)
print(lnk_lst2)
lnk_lst2.insert_sorted(3)
print(lnk_lst2)
'''

if __name__ == "__main__":
	import doctest
	doctest.testmod()