class LinkedListNode(object):
    ''' a simple Linked List class'''
    def __init__(self, data):
        self.next = None
        self.data = data

def reverseLinkedListNotInPlace(head_node):
    ''' reverses a linked list by creating a new linked list'''
    current = head_node
    new_head = None
    prev = None
    while current: 
        new_node = LinkedListNode(current.data)
        new_node.next = prev
        prev = new_node
        current = current.next 
    return prev

A= LinkedListNode('A')
B = LinkedListNode('B')
C = LinkedListNode('C')
D = LinkedListNode('D')

A.next = B
B.next = C
C.next = D
D.next = None

def print_nodes(head_node):
    ''' prints all the nodes in sequence '''
    current = head_node
    while current:
        print(current.data)
        current = current.next

