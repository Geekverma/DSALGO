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
        '''Print the list element'''
        
        while self is not None:
            yield self.data
            self = self.next




a = Node(5)
b = Node(7)
c = Node(9)

a.next = b
b.next = c
c.next = None

value = a.print_list()
print(next(value))
print(next(value))
print(next(value))




# s = sum_of_list(a)
# print(f'sum of nodes are {s}')

# a = Node("a")
# b = Node("c")
# c = Node("g")

# a.next = b
# b.next = c
# c.next = None
# c = create_list(a)
# print(c)



# def sum_of_list(node):
#     '''sum the nodes and output the result'''
#     sum = 0
#     while node is not None:
#         sum+=node.data
#         node=node.next

#     return sum