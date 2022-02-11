'''Linkedlist Programe to sum the element of the node.
1->2->3->4->5
head = Null
tail = Null
| 1|->| |2|->|


1 2 3 4 5-> how to pass them as input.

either create an object for each node?
n = Node()

print(n.next)
n.data = 5
print(n.data)

you can join them consecuently with in function or class with Node class as template for each node.


'''




class Node(object):

    def __init__(self,data) -> None:
        self.data = data
        self.next = None


    def print_list(self):
        '''Print the list element
        using genarator 
        '''
        while self is not None:
            yield self.data
            self = self.next

    def print_element_of_node(self):
        return self.data


    def insert_node_at_tail(self, head):
        '''insert node at tail'''
        while head.next is not None:
            head = head.next

        head.next = self
        self.next = None


    def insert_node_at_head(self, head):
        '''insert node at head'''
        self.next = head


    def inset_between_the_nodes(self, first_node, second_node):
        ''' insert between the first and second node'''

        first_node.next = self
        self.next = second_node

        
        

a = Node(5)
b = Node(7)
c = Node(9)
d = Node(12)
e = Node(11)
f = Node(3)
a.next = b
b.next = c
c.next = None


d.insert_node_at_tail(a)
e.insert_node_at_head(a)
f.inset_between_the_nodes(b,c)
value = e.print_list()
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))






