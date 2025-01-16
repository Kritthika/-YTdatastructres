from LinkedList import LinkedList, Node

def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False
    
    lenA = len(llA)
    lenB = len(llB)
    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)
    shorterNode = shorter.head
    longerNode = longer.head
    for i in range(diff):
        longerNode = longerNode.next
    
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    return longerNode
def addsame(llA, llB, value):
    temp_node = Node(value)
    llA.tail.next = temp_node
    llA.tail = temp_node
    llB.tail.next = temp_node
    llB.tail = temp_node
llA = LinkedList()
llB = LinkedList()
llA.generate(4,0,10)
llB.generate(3,0,10)
print(llA)
print(llB)
addsame(llA,llB,3)
addsame(llA, llB, 5)
print(llA)
print(llB)
print(f"Length of List A: {len(llA)}")
print(f"Length of List B: {len(llB)}")
print(f"Tail of List A: {llA.tail}")
print(f"Tail of List B: {llB.tail}")

print(intersection(llA, llB))
