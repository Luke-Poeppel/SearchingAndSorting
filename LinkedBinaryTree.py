'''
Linked Binary Tree
'''
	
class LinkedBinaryTree(object):
	class Node(object):
		def __init__(self, data, left = None, right = None):
			self.data = data
			self.parent = None

			self.left = left
			if left is not None:
				left.parent = self
			
			self.right = right
			if right is not None:
				right.parent = self

	def __init__(self, root = None):
		'''
		Size: amount of nodes in a tree. Count recursively?
		'''
		self.root = root
		self.size = self.subtree_count(root)

	def subtree_count(self, root):
		if root is None:
			return 0
		else:
			left_count = self.subtree_count(root.left)
			right_count = self.subtree_count(root.right)

			return 1 + left_count + right_count

	def sum(self):
		return self.subtree_sum(self.root)

	def subtree_sum(self, root):
		if root is None:
			return 0
		else:
			left_sum = self.subtree_sum(root.left)
			right_sum = self.subtree_sum(root.right)

			return root.data + left_sum + right_sum

	def height(self):
		'''
		Length of longest path, not literally height.
		'''
		if self.is_empty():
			raise Exception("Tree is empty!")
		else:
			self.subtree_height(self.root)

	def subtree_height(self, root):
		if (root.left is None and root.right is None):
			return 0
		elif root.right is None:
			return 1 + left_height
		elif root.left is None:
			return 1 + right_hight
		else:
			left_height = self.subtree_height(root.left)
			right_hight = self.subtree_height(root.right)

			return 1 + max(left_height, right_hight)

	def __iter__(self):
		'''
		Tree traversal order ideas:
		1.) Pre-Order (DLR: data, left, right)
		2.) In-Order (LDR: left, data, right)
		3.) Post-Order (LRD: left, right, data)
		4.) Level by level order
		'''
		pass



