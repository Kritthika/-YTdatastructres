from LinkedList import LinkedList

def partition(ll, x):
    curnode = ll.head
    ll.tail = ll.head
    while curnode:
        nextnode = curnode.next
        curnode.next = None
        if curnode.value < x:
            curnode.next = ll.head
            ll.head = curnode
        else:
            ll.tail.next = curnode
            ll.tail = curnode
        curnode = nextnode
    if ll.tail.next is not None:
        ll.tail.next = None

llpart = LinkedList()
llpart.generate(5, 0, 40)
print(llpart)
partition(llpart, 30)
print(llpart)
        
