class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLL(object):
    """Singly linked list (SLL) data structure with insert, delete, search and show functions."""
    def __init__(self):
        self.head = None

    def delete(self, node):
        """Cannot delete the head of the SLL"""
        trav1 = self.head
        if trav1.next is not None:
            trav2 = trav1.next
        else:
            if trav1.data == node:
                self.head = trav1.next
                return print('Deleted', node)
            else:
                return print(node, 'not in list to be deleted')
        while trav2.next is not None:
            if trav2.data == node:
                trav1.next = trav2.next
                return print('Deleted', node)
            else:
                trav1 = trav1.next
                trav2 = trav2.next
        else:
            if trav2.data == node:
                trav1.next = trav2.next
                return print('Deleted', node)
            else:
                return print(node, 'not in list to be deleted')

    def insert(self, node):
        trav = self.head
        while trav.next is not None:
            trav = trav.next
        trav.next = Node(node)

    def search(self, node):
        trav = self.head
        p = 0
        while trav.data != node and trav.next is not None:
            p = p + 1
            trav = trav.next
        if trav.data == node:
            print(node, 'is in position', p)
        else:
            print(node, 'was not found')

    def show(self):
        trav = self.head
        while trav.next is not None:
            print(trav.data, '- ', end='')  # no new lines are printed
            trav = trav.next
        print(trav.data)  # prints last node and a new line

    def sort(self, direction='descending'):
        """Set direction to ascending to get ascending order and to descending to get descending order."""
        if direction == 'descending':
            direction = '<'
        elif direction == 'ascending':
            direction = '>'
        swap_needed = True
        while swap_needed:
            trav1 = self.head
            if trav1.next is not None:
                trav2 = trav1.next
            else:
                return print('Because linked list has exactly one node list cannot'
                             ' be sorted')
            while trav2.next is not None or str(trav1.data) + direction + str(trav2.data):
                if eval(str(trav1.data) + direction + str(trav2.data)):  # either a >, or a < comparison is made
                    # if trav1.data > trav2.data:
                    temp = trav1.data
                    trav1.data = trav2.data
                    trav2.data = temp
                    swap_needed = True
                    break
                else:
                    swap_needed = False
                    trav1 = trav1.next
                    if trav2.next is not None:
                        trav2 = trav2.next
                    else:
                        break


llist = SLL()
llist.head = Node(8)
llist.insert(3)
llist.insert(7)
llist.show()
llist.search(3)
llist.delete(7)
llist.show()
llist.search(10)
llist.insert(7)
llist.insert(2)
llist.sort()
llist.show()
llist.sort('ascending')
llist.show()
