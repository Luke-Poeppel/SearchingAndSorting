'''
Linked Binary Tree
'''

from Queue import ArrayQueue
	
class LinkedBinaryTree(object):
	'''
	Linked Binary Tree Object.

	>>> node1 = LinkedBinaryTree.Node(1)
	>>> node2 = LinkedBinaryTree.Node(2)
	>>> node3 = LinkedBinaryTree.Node(3, left = node1, right = node2)
	>>> node4 = LinkedBinaryTree.Node(4)
	>>> node5 = LinkedBinaryTree.Node(5)
	>>> node6 = LinkedBinaryTree.Node(6, left = node4, right = node5)
	>>> rt = LinkedBinaryTree.Node(10, left = node3, right = node6)

	>>> lbt = LinkedBinaryTree(rt)
	>>> for thisValue in lbt.inorder():
	...	    print(thisValue.data)
	1
	3
	2
	10
	4
	6
	5
	'''
	class Node(object):
		'''
		Node Object.
		'''
		def __init__(self, data, left = None, right = None):
			self.data = data
			self.parent = None

			self.left = left
			if self.left is not None:
				self.left.parent = self
			
			self.right = right
			if self.right is not None:
				self.right.parent = self

	def __init__(self, root = None):
		'''
		Initializes a Binary Tree.
		'''
		self.root = root
		self.size = self.subtree_count(root)

	def __len__(self):
		'''
		Returns the number of elements in a Binary Tree.
		'''
		return self.size

	def is_empty(self):
		'''
		Returns True if the number of elements in the Tree is 0.
		'''
		return (len(self) == 0)

	def subtree_count(self, root):
		'''
		Counts the number of subtrees originating from a root.
		'''
		if root is None:
			return 0
		else:
			left_count = self.subtree_count(root.left)
			right_count = self.subtree_count(root.right)

			return 1 + left_count + right_count

	def sum(self):
		'''
		Returns the sum of the values in a sub-Tree.
		'''
		return self.subtree_sum(self.root)

	def subtree_sum(self, root):
		'''
		Helper function for sum()
		'''
		if root is None:
			return 0
		else:
			left_sum = self.subtree_sum(root.left)
			right_sum = self.subtree_sum(root.right)

			return root.data + left_sum + right_sum

	def height(self):
		'''
		Returns the height of the Binary Tree (i.e. length of longest path)
		'''
		return self.subtree_height(self.root)

	def subtree_height(self, root):
		if (root.left is None and root.right is None):
			return 0
		elif root.left is None:
			return 1 + self.subtree_height(root.right)		
		elif root.right is None:
			return 1 + self.subtree_height(root.left)
		else:
			left_height = self.subtree_height(root.left)
			right_hight = self.subtree_height(root.right)

			#Use max to get *longest* path.
			return 1 + max(left_height, right_hight)

	def preorder(self):
		yield from self.subtree_preorder(self.root)
	
	def subtree_preorder(self, root):
		if root is None:
			return
		else:
			yield root
			yield from self.subtree_preorder(root.left)
			yield from self.subtree_preorder(root.right)

	def postorder(self):
		yield from self.subtree_postorder(self.root)

	def subtree_postorder(self, root):
		if root is None:
			return
		else:
			yield from self.subtree_postorder(root.left)
			yield from self.subtree_postorder(root.right)
			yield root

	def inorder(self):
		yield from self.subtree_inorder(self.root)

	def subtree_inorder(self, root):
		if root is None:
			return
		else:
			yield from self.subtree_inorder(root.left)
			yield root
			yield from self.subtree_inorder(root.right)

	def breadth_first(self):
		if self.is_empty():
			return
		line = ArrayQueue()
		line.enqueue(self.root)

		while (line.is_empty() == False):
			curr_node = line.dequeue()
			yield curr_node
			if curr_node.left is not None:
				line.enqueue(curr_node.left)
			if curr_node.right is not None:
				line.enqueue(curr_node.right)

	def __iter__(self):
		'''
		Tree traversal order ideas:
		1.) Pre-Order (DLR: data, left, right)
		2.) In-Order (LDR: left, data, right)
		3.) Post-Order (LRD: left, right, data)
		4.) Level by level order
		'''
		for node in self.breadth_first:
			yield node.data

if __name__ == '__main__':
	import doctest
	doctest.testmod()