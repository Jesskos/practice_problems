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


