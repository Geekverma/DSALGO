class MyList:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def print_list(head):
        while head:
            print(head.val, end=" ")
            head = head.next
    
    def revers_list(head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        # while prev:
        #     print(prev.val, end=" ")
        #     prev = prev.next
            
    def mid_node(head):
        fast = head
        slow = head
        
        while fast!=None and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow, fast

    def is_palindrom(head):
        '''to check list is palindrom or not, find the middle and revers the second half the check val of head and mid consecutively'''
        if head.next == None:
            return True
        else:
            #for even len list fast is at None and for odd list fast is at last node
            mid,fast = head.mid_node()

            if fast is None:
                #for even list
                mid = mid.revers_list()
            elif fast is not None:
                #for odd list
                mid = mid.next.revers_list()

            ptr = head
            while mid:
                if ptr.val != mid.val:
                    return False
                ptr = ptr.next
                mid = mid.next
        return True
            






a = MyList(1)
b = MyList(0)
c = MyList(3)
d = MyList(4)
e = MyList(0)
f = MyList(1)
# g = MyList(1)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = None
# g.next = None

a.print_list()
print("#"*10)
# a.mid_node()
# print("#"*10)
# a.revers_list()
print(a.is_palindrom())