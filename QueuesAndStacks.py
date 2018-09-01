
class Stack(object):
	''' a stack object with methods, push, pop  ''' 
	def __init__(self):
		self._stack = []

	def push(self, element):
		self._stack.append(element)

	def pop(self):
		if self._stack:
			el = self._stack.pop()
			return el

	def peek(self):
		return self._stack[-1]

	def is_empty(self):
		if not self._stack:
			return True
		else:
			return False


	def print_stack(self):
		print self._stack


class QueueStack(object):
	''' a queue object made with queue functionality using stack methods ''' 

	def __init__(self):
		self.my_stack_enqueue = Stack()
		self.my_stack_dequeue= Stack()

	def enqueue(self, item):
		''' adds item to the end of the queue'''
		self.my_stack_enqueue.push(item)

	def dequeue(self):
		''' removes item from beginning of queue using implemented second stack '''
		if self.my_stack_dequeue.is_empty():
			while not self.my_stack_enqueue.is_empty(): 
				item = self.my_stack_enqueue.pop()
				self.my_stack_dequeue.push(item)
		
		removed_item = self.my_stack_dequeue.pop()
		return removed_item


	def print_queue(self):
		print self.my_stack_enqueue.print_stack()
		print self.my_stack_dequeue.print_stack()




class Queue(object):
	''' a simple queue made using a regular Python list. Although a Linked List is preferable, this is made for ease'''
	def __init__(self):
		self._queue = []

	def enqueue(self, item):
		self._queue.append(item)

	def dequeue(self):
		if self._queue:
			self._queue.pop(0)

	def front(self):
		if self.print_queue:
			return self._queue[0]

	def is_empty(self):
		if not self._queue:
			return True
		else:
			return False

	def print_queue(self):
		print self._queue

class StackQueue(object):
	''' A stack made from using queue methods '''

	def __init__(self):
		self.my_stack_push = Queue()
		self.my_stack_pop = Queue()


	def push(self, item):
		self.my_stack_push.enqueue(item)

	def pop(self):
		if self.my_stack_pop.is_empty():
			item = self.my_stack_push.dequeue()
			self.my_stack_pop.enqueue(item)
		popped_item = self.my_stack_pop.dequeue()
		return popped_item


	def print_stack(self):
		print self.my_stack_push.print_queue()
		print self.my_stack_pop.print_queue()



class MinStack(object):
	def __init__(self):
		''' a main stack to keep track of all nums and supporting stack to keep track of minimums'''
		self._stack = []
		self._supporting = []

	def push(self, x):
		''' adds new top element to main stack. If new element is less than the current top element 
		in supporting stack, appends this element to top to become new minimum. Else, adds re-adds 
		current top (minimum) to supporting stack''' 

		self._stack.append(x)

		if self._supporting:
			minimum = self.getMin()
			if x < minimum:
				self._supporting.append(x)
			else:
				self._supporting.append(minimum)

		else:
			self._supporting.append(x)


	def pop(self):
		''' removes top element of main stack and supporting stack ''' 
		self._stack.pop()
		self._supporting.pop()

	def top(self):
		''' gets the top element from the main stack ''' 
		if self._supporting:
			return self._supporting[-1]
		else:
			return -1

	def getMin(self):
		''' gets the minimum from the supporting stack, which is always the top element''' 
		if self._supporting:
			return self._supporting[-1]
		else:
			return -1




