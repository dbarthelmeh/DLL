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
                if trav.next is not None:
                    trav.previous.next = trav.next
                    trav.next.previous = trav.previous
                    del trav
                    return print('Deleted', targeted_data)
            else:
                trav = trav.next

        # if trav.next is not None:
        #     trav = trav.next
        # else:
        #     if trav.data == targeted_data:
        #         self.head = trav.next
        #         return print('Deleted', targeted_data)
        #     else:
        #         return print(targeted_data, 'not in list to be deleted')
        # while trav2.next is not None:
        #     if trav2.data == targeted_data:
        #         trav.next = trav2.next
        #         return print('Deleted', targeted_data)
        #     else:
        #         trav = trav.next
        #         trav2 = trav2.next
        # else:
        #     if trav2.data == targeted_data:
        #         trav.next = trav2.next
        #         return print('Deleted', targeted_data)
        #     else:
        #         return print(targeted_data, 'not in list to be deleted')

    def insert(self, node_data):
        trav = self.head
        while trav.next is not None:
            trav = trav.next
        trav.next = Node(node_data)
        trav.next.previous = trav

    def search(self, node_data):
        trav = self.head
        p = 0
        while trav.data != node_data and trav is not None:
            p = p + 1
            trav = trav.next
        if trav.data == node_data:
            print(node_data, 'is in position', p)
        else:
            print(node_data, 'was not found')

    def show(self):
        trav = self.head
        while trav.next is not None:
            print(trav.data, '- ', end='')  # no new lines are printed
            trav = trav.next
        print(trav.data)  # prints last node and a new line

    def sort(self, order='descending'):
        """Set direction to ascending to get ascending order and to descending to get descending order."""
        if order == 'descending':
            order = '<'
        elif order == 'ascending':
            order = '>'
        swap_needed = True
        while swap_needed:
            trav = self.head.next
            while trav is not None:
                if eval(str(trav.previous.data) + order + str(trav.data)):
                    temp = trav.data
                    trav.data = trav.previous.data
                    trav.previous.data = temp
                    break
                else:
                    trav = trav.next
            if trav is None:  # we've completed the previous loop with no swaps
                swap_needed = False

            # if trav1.next is not None:
            #     trav2 = trav1.next
            # else:
            #     return print('Because linked list has exactly one node list cannot'
            #                  ' be sorted')
            # while trav2.next is not None or str(trav1.data) + direction + str(trav2.data):
            #     if eval(str(trav1.data) + direction + str(trav2.data)):  # either a >, or a < comparison is made
            #         # if trav1.data > trav2.data:
            #         temp = trav1.data
            #         trav1.data = trav2.data
            #         trav2.data = temp
            #         swap_needed = True
            #         break
            #     else:
            #         swap_needed = False
            #         trav1 = trav1.next
            #         if trav2.next is not None:
            #             trav2 = trav2.next
            #         else:
            #             break


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
