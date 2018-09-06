class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right



def make_bst(nums):
    """Given a list of sorted numbers, make a binary search tree.

    Returns the root node of a new BST that is valid and balanced.


    """

    if not nums:
    	return None

    midpoint = len(nums)/2
    node = BinaryNode(nums[midpoint])

    node.left = make_bst(nums[:midpoint])
    node.right = make_bst(nums[midpoint+1:])

    return node





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n**** ALL TESTS PASSED. YOU'RE A TREE-MASTER!\n")