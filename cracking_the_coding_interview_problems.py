def all_unique(str):
	''' check if all characters are unique without using additional data structures ''' 
	for idx, char in enumerate(str):
		str = str.lower()
		if char in str[:idx] or char in str[idx+1:]:
			return False
	return True 

def is_permutation_of_word(word1, word2):
	''' checks if two words are permutations of eachother '''
	if word1 == word2:
		return False
	letter_count_dictionary_word1= {}
	letter_count_dictionary_word2= {}
	for letter in word1:
		letter_count_dictionary_word1[letter] = letter_count_dictionary_word1.get(letter, 0) + 1 
	for letter in word2:
		letter_count_dictionary_word2[letter] = letter_count_dictionary_word2.get(letter, 0) + 1
	if letter_count_dictionary_word1 != letter_count_dictionary_word2:
		return False
	return True 



def urlify(phrase):
	empty_str = ""
	''' replaces all strings in a phrase with %20 ''' 
	phrase_list = phrase.split(" ")
	return "%20".join(phrase_list)

def is_palindome_permutation(phrase):
	'''' checks if a phrase is a permutation of a pallindorme'''

	letter_count_dictionary = {}
	for letter in phrase:
		letter_count_dictionary[letter.lower()] = letter_count_dictionary.get(letter.lower(), 0) + 1 
	letters_occurring_odd_num_times = 0 
	for letter in letter_count_dictionary:
		if letter_count_dictionary[letter] % 2 != 0 and letter != " ":
			letters_occurring_odd_num_times +=1 
	if letters_occurring_odd_num_times > 1:
		return False
	else:
		return True

def one_edit_away(word1, word2):
	''' determines whether or not two strings are one or less edits away, with edits defined as adding, removing, or replacing '''
	# insert
	# remove

	# replace
	if word1 == word2:
		return True 
	count = 0  
	for idx, char in enumerate(word1):
		word2_modification = word2[:idx] + char + word2[idx+1:]
		if word1 == word2_modification:
			return True 

	# remove char and add character
	for idx, char in enumerate(word1):
		word1_modification = word1[:idx] + word1[idx+1:]
		if word1_modification == word2:
			return True

	for idx, char in enumerate(word2):
		word2_modification = word2[:idx] + word2[idx+1:]
		if word2_modification == word1:
			return True

	def rotate_matrix(matrix):
		''' Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. (an you do this in place?
		>>> [[1,2,3,4], 
			[5,6,7,8], 
			[9,10,11,12], 
			[13,14,15,16]]
		'''
			
		# i = 0
		# j = 3

		# for idx, row in enumerate(matrix):
		# 	for idx, num in enumerate(row):
		# 		matrix[]

class LinkedList(object):

	def __init__(self):
		self.head = None 
		self.tail = None 

	def print_list(self):
		current = self.head 
		while current != None:
			print current.data
			current = current.next 

	def remove_duplicates(self):
		''' 2.1 a method to remove nodes with duplicate pieces of data''' 
		seen = [self.head.data]
		current = self.head 
		while current != None:
			if current.next != None:
				if current.next.data not in seen:
					seen.append(current.next.data)
				else:
					current.next = current.next.next

			current = current.next

	def get_length_of_list(self):
		''' a mathod on linked list class to get length '''
		count = 0 
		current = self.head 
		while current:
			count += 1
			current = current.next
		return count 

	def find_n_to_last_element(self, n_to_last):
		''' 2.2 a method that returns the n to last node of a linked list. If n_to_last longer than list, returns None'''

		length = self.get_length_of_list()
		forward_num = length - n_to_last
		previous = None 
		current = self.head
		count = 0 
		while count <= forward_num: 
			previous = current 
			current = current.next
			count += 1 
		if previous: 
			return previous.data
		else:
			return previous

	def delete_middle_node(self, node):
		''' deletes a node in the middle given access to only one node. If node not in the middle, list not changes''' 

		if self.head != node and node.next != None:
			current = self.head
			while current != node:
				previous = current
				current = current.next 
				if current == node:
					previous.next = current.next 




class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None


dog = Node('dog')
cat = Node('cat')
bear = Node('bear')
lion = Node('lion')
bird = Node('bird')
dog.next = cat
cat.next = bear
bear.next = lion
lion.next = bird
animals = LinkedList()
animals.head = dog

print animals.find_n_to_last_element(3)
blue = Node('blue')
colors = LinkedList()
colors.head = blue




if __name__ == "__main__":
    import doctest
    doctest.testmod()











		


