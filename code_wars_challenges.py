
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

    """

    binary_str = ""
    if num == 0:
        return 0
    while num:
        if num % 2 == 0:
            binary_str = '0' + binary_str
        else:
            binary_str = '1' + binary_str
    return binary_str 



    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

