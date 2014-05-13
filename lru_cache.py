
class LRUCache(object):

	def __init__(self, size):
		self.size = size
		self.hashtable = {}
		self.list_size = 0
		self.linked_list = LinkedList()

	def _purge_list(self):
		if self.list_size > self.size:
			key = self.linked_list.head.key
			self.linked_list.remove_node(0)
			del self.hashtable[key]
			
	def cache(self, key, value):
		if key not in self.hashtable:
			self.hashtable[key] = value
			self.linked_list.add_node(key, value)
			self.list_size += 1
		else:
			return self.self.hashtable[key]
		self._purge_list()	
		print self.linked_list.print_list_forward()
		return self.hashtable, self.hashtable[key] 


class Node(object):

	def __init__(self, key, data):
		self.key = key
		self.data = data
		self.next = None
		self.prev = None

class LinkedList(object):

	def __init__(self):
		self.head = None
		self.tail = None

	def add_node(self, key, data):
		node = Node(key, data)

		if self.head == None:
			self.head = node

		if self.tail != None:
			self.tail.next = node
			node.prev = self.tail	

		self.tail = node	

	def remove_node(self, index):
		counter = 0
		node = self.head 

		while counter < index: 
			node = node.next
			counter += 1	
		
		if node == self.head:
			self.head = node.next
			self.head.prev = None

		elif node == self.tail:
			self.tail = node.prev
			self.tail.next = None	

		else:	
			node.prev.next = node.next
			node.next.prev = node.prev

			
	def find_data(self, key):
		node = self.head
		counter = 0
		while node != None:
			print node.data
			counter += 1
			if node.key == key:
				return counter
			node = node.next
		return False

	def print_list_forward(self):
		node = self.head
		while node != None:
			if node.data != None:
				print node.data
				node = node.next

	def print_list_backward(self):
		node = self.tail
		while node != None:
			if node.data != None:
				print node.data
				node = node.prev		




				