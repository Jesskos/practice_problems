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








		


