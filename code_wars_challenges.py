from random import choice 

def to_camel_case(str):
    """ Converts a string to Camel Case with underscores and hyphens (from codewars)

        >>> to_camel_case('')
        ''
        >>> to_camel_case('the_stealth_warrior')
        'theStealthWarrior'

        >>> to_camel_case('The-Stealth-Warrior')
        'TheStealthWarrior'

        >>> to_camel_case('A-B-C')
        'ABC'

    """

    list_of_words = str.split("-")
    new_list_of_words = []
    for word in list_of_words:

        if "_" in word:
            new_words = word.split("_")
            new_list_of_words.extend(new_words)
        else: 
            new_list_of_words.append(word)
        
    new_str = "" + new_list_of_words[0]

    for word in new_list_of_words[1:]:
        new_word = word.title()
        new_str += new_word 

    return new_str

def dec2bin(num):
    """Convert a decimal number to binary representation.
    >>> dec2bin(6)
    '110'
    >>> dec2bin(2)
    '10'
    >>> dec2bin(4)
    '100'
    >>> dec2bin(0)
    '0'
    >>> dec2bin(1)
    '1'
    >>> dec2bin(10)
    '1010'
    >>> dec2bin(8)
    '1000'


    """

    binary_str = ""
    if num == 0:
        return '0'
    while num:
        if num % 2 == 0:
            binary_str = '0' + binary_str
        else:
            binary_str = '1' + binary_str
        num = num/2
    return binary_str 


def maxSequence(arr):
    ''' The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

    >>> maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6 
    maxSequence([])
    0 
    '''

def is_prime(num):
    ''' returns True if number is prime 
    >>> is_prime(2)
    True
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(1)
    False
    ''' 


    i = 2
    if num == 2:
        return True
    if num == 1 or num == 0:
        return False
    if num < 0: 
        return False 
    while i < num:
        if num % i  == 0:
            return False
        i += 1 
    return True 
      

def done_or_not(board): #board[i][j]

    ''' checks whether or not a sudoku board is correct
    >>> done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]])
    'Finished!'

    >>> done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]])
    'Try again!'
    
    '''
def done_or_not(board): #board[i][j]
  # checking each row
    for row in board:
        if len(set(row)) != 9:
            return 'Try again!'
          
  # checking each column 
    i = 0
    while i <= 8:
        column = []
        for row in board:
            column.append(row[i])
        if len(set(column)) != 9:
            return 'Try again!' 
        i += 1
  
  # checking each 3 by 3 square

    x1 = 0
    x2 = 3

    while x1 <= 6:
        y1 = 0 
        y2 = 3
        while y1 <= 6:
            box = []
            for row in board[x1:x2]:
                box.extend(row[y1:y2])
            if len(set(box)) != 9:
                return 'Try again!'
            y1 += 3
            y2 += 3 
        x1 += 3
        x2 += 3
              
  
    return 'Finished!'

def order_weight(strng):
    ''' orders a str of weights based on sum of digits 
    >>> order_weight("103 123 4444 99 2000")
    '2000 103 123 4444 99'

    >>> order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")
    '11 11 2000 10003 22 123 1234000 44444444 9999'

    '''
    list_of_weights = strng.split(" ")
    weight_list_updated = []
    final_str = ""
    for weight in list_of_weights:
        sum = 0 
        weight_digits = list(weight)
        for digit in weight_digits:
            sum += int(digit)
        weight_list_updated.append((sum, weight))
    weight_list_updated.sort()
    for weight in weight_list_updated:
        final_str = final_str + str(weight[1]) + " "
    return final_str[0:-1]
    
def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    >>> lst = ["hey", "there", "you"]
    >>> recursive_index("porcupine", lst) is None
    True
    >>> recursive_index("you", ["hey", "there", "you"])
    2
    >>> recursive_index("there", ["hey", "there", "you"])
    1

    """

    if not haystack:
        return None

    item = haystack.pop()
    if item == needle:
        print len(haystack)
    else:
        return recursive_index(needle, haystack)

class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_string(self):
        """Represent data for this node and it's successors as a string.

        >>> Node(3).as_string()
        '3'

        >>> Node(3, Node(2, Node(1))).as_string()
        '321'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)

def remove_node(node):
    """Given a node in a linked list, remove it.

    Remove this node from a linked list. Note that we do not have access to
    any other nodes of the linked list, like the head or the tail.

    Does not return anything; changes list in place.
    """

    node.data = node.next.data
    node.next = node.next.next 


def print_recursively(lst):
    """Print items in the list, using recursion."""

    if not lst:
        return 

    print lst[0]

    print print_recursively[lst[1:]]

def count_recursively(lst):
    """Return number of items in a list, using recursion."""

    if not lst:
        return 0 

    if lst:
        return count_recursively(lst[1:]) + 1


def valid_parentheses(string):
    brackets = []
    for char in string:
        if char == "(":
            brackets.append("(")
        elif char == ")":
            if brackets:
               brackets.pop()
            elif not brackets:
                return False
    if not brackets:
        return True
    return False 

def sum_list(nums):
    """Using recursion, return the sum of numbers in a list."""

    if not nums:
        return 0 

    if nums:
        num = nums.pop()
        return sum_list(nums) + num
def split(astring, splitter):

    """Split a string by splitter and return list of splits.
    >>> split("my dog's name is teddy", "d")
    ['my ', "og's name is te", '', 'y']
    >>> split('colorful', 'l')
    ['co', 'orfu', '']
    >>> split('', '')
    []
    """

    splits = []
    last_idx = 0
    i = 0 
    while i < len(astring):
        if astring[i] == splitter:
            splits.append(astring[last_idx:i])
            last_idx = i + 1 
        if i == len(astring)-1:
            splits.append(astring[last_idx:])
        i += 1 
    return splits

def hour_glass_sum(grid): 
    """ Find max hourglass sum in a grid 
    >>> hour_glass_sum([[1,2,3,1,1,1], [3,4,5,1,1,1], [6,7,8,0,0,0], [9,8,7,0,0,0], [7,7,7,1,1,1], [9,9,9,0,0,0]])
    58
    """
    sum_list = []
    for row_index in range(len(grid)-2):
        for num_index in range(len(grid)-2):
            hourglass_sum = sum(grid[row_index][num_index:num_index+3]) + grid[row_index+1][num_index+1] + sum(grid[row_index+2][num_index:num_index+3])
            sum_list.append(hourglass_sum)
    return max(sum_list)

#     sums = []

#     max = None 

#     for i in range(len(grid)-2):
#         for j in range(len(grid)-2):
#             hourglass_sum = sum(grid[i][grid[j:j+3]]) + sum(grid[i+1][j+1]) + sum(grid[i+2][j+2])



def is_palindrome(word):
    """Return True/False if this word is a palindrome.
    >>> is_palindrome("a")
    True

    >>> is_palindrome("noon")
    True

    >>> is_palindrome("racecar")
    True

    >>> is_palindrome("porcupine")
    False

    >>> is_palindrome("Racecar")
    False

    """

    i = 0 
    while i < len(word) / 2: 
        if word[i] != word[len(word)-i-1]:
            return False
        i += 1 
    return True 

def binary_search_recursively(arr, num, right_array_factor=0):
    ''' recursively searches a sorted array for the index of a number within that array, and returns the index
    >>> binary_search_recursively([1,2,3,4,5], 0)
    'number not found'
    >>> binary_search_recursively([1,2,3,4,5], 6)
    'number not found'
    >>> binary_search_recursively([1,2,3,4,5], 5)
    4
    >>> binary_search_recursively([1,2,3,4,5], 1)
    0
    ''' 

    midpoint = len(arr)/2
    if arr: 
        if arr[midpoint] > num:
            return binary_search_recursively(arr[:midpoint], num)
        elif arr[midpoint] < num:
            right_array_factor = len(arr[:midpoint+1])
            return binary_search_recursively(arr[midpoint+1:], num, right_array_factor)
        elif arr[midpoint] == num:
            return midpoint + right_array_factor
    else:
        return "number not found"

def find_pivot_point(arr):
    ''' finds the pivot point in a sorted array shifted n places. Pivot point defined as index
    where decrease occurs after increase in integers. if no shift in array, returns None ''' 
    for index in range(len(arr)):
        if arr[index+1]<arr[index]:
            return index + 1 

    return None 

# def find_pivot_point_binary_searcg(arr):
#     ''' same as above but finds the pivot point index using binary search 

#     find_pivot_point_binary_searcg([4,5,6,7,8,1,2]
#     5
#     find_pivot_point_binary_searcg([8,1,2,3,4,5,6]
#     1

#     '''
#     low_index = 0 
#     high_index = len(arr)-1 
#     midpoint = (high - low)/2
#     while begin <= end:
#         midpoint = (high - low)/2 + low 
#         if arr[midpoint] < arr[midpoint-1]:
#             return midpoint 
#         elif arr[midpoint] > arr[midpoint-1]:
#             high_index += 1 
#         elif arr[midpoint]  arr[midpoint-1]:
#             high_index += 1 




#     def binary_search_shifted_arr(arr, num):
#     pivot_point = find_pivot_point(arr)
#     arr_left = arr[:pivot_point]
#     arr_right = arr[pivot_point:]
#     binary_search_result_left = binary_search_recursively(arr_left, num)
#     if binary_search_result_left != "number not found":
#         return binary_search_result
#     else:
#         return binary_search_recursively(arr_right, num)


def binary_search(val):
    """Using binary search (non-recursively), find val in range 1-100. Return # of guesses.
    >>> binary_search(10)
    6
    >>> binary_search(50)
    1
    >>> binary_search(87)
    7



    """

    assert 0 < val < 101, "Val must be between 1-100"

    low = 0 
    high = 101
    num_guesses = 0
    guess = 0 

    while guess != val:
        guess = (high - low)/2 + low 
        if guess > val:
            high = guess 
            num_guesses += 1
        elif guess < val:
            low = guess 
            num_guesses +=1 
        else:
            num_guesses += 1 
            return num_guesses 

def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.

    >>> has_balanced_brackets("(my name is) [teddy]")
    True

    >>> has_balanced_brackets("[[]])")
    False

    >>> has_balanced_brackets("<(][)>}")
    False

    >>> has_balanced_brackets("(()))")
    False

    >>> has_balanced_brackets(">")
    False

    >>> has_balanced_brackets("(This has {too many} ) closers. )")
    False

    """
    
    bracket_dictionary = {"()": [], "[]": [], "{}": [], "<>": []}
    for letter in phrase: 
        for bracket_type in bracket_dictionary:
            if letter in bracket_type and letter in "([{<":
                bracket_dictionary[bracket_type].append(letter)
            elif letter in bracket_type and letter in ")]}>":
                if not bracket_dictionary[bracket_type]:
                    return False
                else:
                    bracket_dictionary[bracket_type].pop()
    for bracket_type in bracket_dictionary:
        if bracket_dictionary[bracket_type]:
            return False
    else:
        return True 

           
def string_operators(str):
    "+-*/**"
    list_of_operators = []
    for item in str:
        if item == "*":
            



if __name__ == "__main__":
    import doctest
    doctest.testmod()

