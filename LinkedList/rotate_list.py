from requests import head


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

        
    def rotate_list(self, k):
        #check if head not None
        if self is None:
            return None
        else:
            curr = self
            node_len=1
            #find len of list
            while curr.next:
                node_len+=1
                curr = curr.next
            
            #connect curr to head that make a list cycle.
            curr.next = self
            # find step to rotate list
            k = k%node_len
            step = node_len-k
            #move curr upto step .
            for _ in range(step):
                curr = curr.next
            
            #define new head
            self = curr.next
            #set curr next to None.
            curr.next = None

            return self



        

a = Node(5)
b = Node(7)
c = Node(9)
d = Node(12)
e = Node(11)
f = Node(3)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = None


value=a.print_list()



print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))


print('#'*10)
print('rotated list')
rotate_list = a.rotate_list(7)

value=rotate_list.print_list()

print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))