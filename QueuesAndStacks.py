
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

class MinStack(object):
    ''' A stack with methods in linear runtime'''
   
    def __init__(self):
        self._stack = []
        self.minimum = None
        
    def push(self, x):
        if not self._stack:
            self.minimum = x
        elif x < self.minimum:
            self.minimum = x
        self._stack.append(x)
            

    # @return nothing
    def pop(self):
        if self._stack:
            self._stack.pop()
        if not self.stack:
        	return -1


	# @return an integer
	def top(self):
		if self._stack:
			return self._stack[-1]
		else:
			return -1
        
    # @return an integer
    def get_min(self):
    	if self.minimum:
    		return self.minimum
    	else:
    		return -1







