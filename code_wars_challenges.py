
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
    

    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

