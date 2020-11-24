class Node(object):
    """Contains info"""
    def __init__(self, data=None):
        self.data = data
        self.next = None  # points to the next node.  This is not data, but the node itself.
        self.previous = None  # points to the previous node


class SLL(object):
    """Singly linked list (SLL) data structure with insert, delete, search and show functions."""
    def __init__(self):
        self.head = None  # the head will be a node object

    def delete(self, targeted_data):
        """Cannot delete the head of the SLL"""
        trav = self.head
        while trav is not None:
            if trav.data == targeted_data:
                if trav.previous is not None:
                    trav.previous.next = trav.next
                    if trav.next is not None:
                        trav.next.previous = trav.previous
                else:
                    self.head = trav.next  # reassign the head
                    if self.head is not None:
                        self.head.previous = None  # head has no previous
                del trav
                return print('Deleted', targeted_data)

            else:
                trav = trav.next

    def insert(self, node_data):
        if self.head is None:
            self.head = Node(node_data)
            return
        trav = self.head
        while trav.next is not None:
            trav = trav.next
        trav.next = Node(node_data)
        trav.next.previous = trav

    def search(self, node_data):
        trav = self.head
        p = 0
        while trav is not None:
            p = p + 1
            if trav.data == node_data:
                return print('Search found that', node_data, 'is in position', p)
            trav = trav.next
        return print(node_data, 'was not found')

    def show(self):
        trav = self.head
        print('List is now ', end='')  # no new lines are printed
        if trav is None:
            return print('so empty')
        while trav.next is not None:
            print(trav.data, '- ', end='')  # no new lines are printed
            trav = trav.next
        print(trav.data)  # prints last node and a new line

    def sort(self, order='descending'):
        """Set direction to ascending to get ascending order and to descending to get descending order."""
        if order == 'descending':
            symbol = '<'
        elif order == 'ascending':
            symbol = '>'
        swap_needed = True
        while swap_needed:
            trav = self.head.next
            while trav is not None:
                if eval(str(trav.previous.data) + symbol + str(trav.data)):
                    temp = trav.data
                    trav.data = trav.previous.data
                    trav.previous.data = temp
                    break
                else:
                    trav = trav.next
            if trav is None:  # we've completed the previous loop with no swaps
                swap_needed = False
            return print('Sorted', order)


llist = SLL()
llist.head = Node(8)
llist.insert(3)
llist.insert(7)
llist.show()
llist.search(3)
llist.delete(7)
llist.show()
llist.delete(3)
llist.delete(8)
llist.show()
llist.insert(8)
llist.insert(3)
llist.show()
llist.search(10)
llist.insert(7)
llist.insert(2)
llist.sort('descending')
llist.show()
llist.sort('ascending')
llist.show()
