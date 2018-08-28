
class Stack(object):
	def __init__(self):
		self._stack = []

	def push(self, element):
		self._stack.append(element)

	def pop(self):
		el = self._stack.pop()
		return el

	def print_stack(self):
		print self._stack

