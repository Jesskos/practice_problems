def all_unique(str):
	''' check if all characters are unique without using additional data structures ''' 
	for idx, char in enumerate(str):
		str = str.lower()
		if char in str[:idx] or char in str[idx+1:]:
			return False
	return True 

def is_permutation_of_word(word1, word2):
	pass 

def urlify(phrase):
	empty_str = ""
	''' replaces all strings in a phrase with %20 ''' 
	phrase_list = phrase.split(" ")
	return "%20".join(phrase_list)


