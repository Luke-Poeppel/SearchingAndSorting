'''
Binary Search Tree Map

Let T be a Binary Tree.
We say that T is a "Binary Search Tree," if for each node n in T:
	1.) All keys stored in the left subtree of n are less than the key stored in n
	2.) All keys stored in the right subtree of n are greater than the key stored in n.
'''

class BinarySearchTreeMap(object):
	class Item(object):
		def __init__(self, key, value = None):
			self.key = key
			self.value = value

	class Node(object):
		def __init__(self, item):
			self.item = item
			self.parent = None
			self.left = None
			self.right = None

		def num_children(self):
			count = 0
			if self.left is not None:
				count += 1
			if self.right is not None:
				count += 1

			return count

		def disconnect(self):
			self.item = None
			self.parent = None
			self.left = None
			self.right = None

	def __init__(self):
		self.root = None
		self.size = 0

	def __len__(self):
		return self.size

	def is_empty(self):
		return (len(self) == 0)

	def __getitem__(self, key):
		node = self.find(key)
		if node is None:
			raise KeyError(str(key) + ' was not found.')
		else:
			return node.item.value

	def find(self, key):
		curr = self.root
		while curr is not None:
			if curr.item.key == key:
				return curr
			elif curr.item.key > key:
				curr = curr.left
			else:
				curr = curr.right

		return None

	def __setitem__(self, key, value):
		node = self.find(key)
		if node is None:
			self.insert(key, value)
		else:
			node.item.value = value

	def insert(self, key, value = None):
		item = BinarySearchTreeMap.Item(key, value)
		new_node = BinarySearchTreeMap.Node(item)

		if self.is_empty():
			self.root = new_node
			self.size = 1
		else:
			parent = self.root
			if key < self.root.item.key:
				curr = self.root.left
			else:
				curr = self.root.right

			while curr is not None:
				parent = curr
				if key < curr.item.key:
					curr = curr.left
				else:
					curr = curr.right

			if key < parent.item.key:
				parent.left = new_node
			else:
				parent.right = new_node

			new_node.parent = parent
			self.size += 1

	def __delitem__(self, key):
		node = self.find(key)
		if node is None:
			raise KeyError(str(key) + ' is not found.')
		else:
			self.delete_node(node)

	def delete_node(self, node_to_delete):
		item = node_to_delete.item
		num_children = node_to_delete.num_children()

		if node_to_delete is self.root:
			if num_children == 0:
				self.root = None
				node_to_delete.disconnect()
				self.size -= 1

			elif num_children == 1:
				if self.root.left is not None:
					self.root = self.root.left
				else:
					self.root = self.root.right
				self.root.parent = None
				node_to_delete.disconnect()
				self.size -= 1

			else:
				max_of_left = self.subtree_max(node_to_delete.left)
				node_to_delete.item = max_of_left.item
				self.delete_node(max_of_left)

		else:
			if num_children == 0:
				parent = node_to_delete.parent
				if node_to_delete is parent.left:
					parent.left = None
				else:
					parent.right = None

				node_to_delete.disconnect()
				self.size -= 1
				
			elif num_children == 1:
				parent = node_to_delete.parent
				if node_to_delete.left is not None:
					child = node_to_delete.left
				else:
					child = node_to_delete.right

				child.parent = parent
				if node_to_delete is parent.left:
					parent.left = child
				else:
					parent.right = child

				node_to_delete.disconnect()
				self.size -= 1

			else:
				max_of_left = self.subtree_max(node_to_delete.left)
				node_to_delete.item = max_of_left.item
				self.delete_node(max_of_left)

		return item

	def subtree_max(self, curr_root):
		node = curr_root
		while node.right is not None:
			node = node.right

		return node

	def inorder(self):
		for node in self.subtree_inorder(self.root):
			yield node

	def subtree_inorder(self, curr_root):
		if curr_root is None:
			pass
		else:
			yield from self.subtree_inorder(curr_root.left)
			yield curr_root
			yield from self.subtree_inorder(curr_root.right)

	def __iter__(self):
		for node in self.inorder():
			yield node.item.key

