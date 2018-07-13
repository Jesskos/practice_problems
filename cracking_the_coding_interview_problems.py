def all_unique(str):
	''' check if all characters are unique without using additional data structures ''' 
	for idx, char in enumerate(str):
		str = str.lower()
		if char in str[:idx] or char in str[idx+1:]:
			return False
	return True 

