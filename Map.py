'''
The Map ADT

Model: A collection of values, each mapped by a key.
Operations:
- m = Map()
- m[k] = v
- m[k]
- del m[k]
- len(m)
- iter(m)

Examples:
m = Map()
m.insert('mk14', 2.5)
m.insert('stb315', 3.7)
m.find('mk14')
2.5
m.delete('stb315')
m['mk14'] = 2.9
'''

class UnsortedArrayMap(object):
	class Item(object):
		def __init__(self, key, value = None):
			self.key = key
			self.value = value

	def __init__(self):
		self.table = []

	def __len__(self):
		return len(self.table)

	def is_empty(self):
		return (len(self) == 0)

	def __getitem__(self, key):
		for item in self.table:
			if item.key == key:
				return item.value
		raise KeyError('Key not in Map.')

	def __setitem__(self, key, value):
		for item in self.table:
			if item.key == key:
				item.value = value
				return
		new_item = UnsortedArrayMap.Item(key, value)
		self.table.append(new_item)
		
	def __delitem__(self, key):
		for i in range(len(self.table)):
			if key == self.table[i].key:
				self.table.pop(i)
				return
		raise KeyError('Key not in Map.')

	def __iter__(self):
		for item in self.table:
			yield item.key

if __name__ == '__main__':
	import doctest
	doctest.testmod()
