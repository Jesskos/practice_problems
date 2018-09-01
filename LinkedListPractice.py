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

def getLinkedList():
    A= LinkedListNode('A')
    B = LinkedListNode('B')
    C = LinkedListNode('C')
    D = LinkedListNode('D')
    E = LinkedListNode('E')

    A.next = B
    B.next = C
    C.next = D
    D.next = E
    E.next = None
    return A

def print_nodes(head_node):
    ''' prints all the nodes in sequence '''
    current = head_node
    while current:
        print(current.data)
        current = current.next

def reverseLinkedListInPlace(head_node):
    ''' Reverses A linked List in place'''

    current = head_node
    prev = None

    while current:
        print current.data
        next = current.next
        current.next = prev
        prev = current
        current = next    

    return prev

