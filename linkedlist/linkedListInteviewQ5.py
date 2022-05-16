# Given two(singly) linked lists, determin f the two list
#  intesect. return the intersecting node. Note tha the
# intersection defined based on the reference, not value.
# that is if the kth node of the the first linked list is
#  the exact same node( by reference) as the jth node of
# the second linked list, then the are intersecting.

from platform import node
from linkedlist import LinkedList, Node


def intersection(llA, llB):
    nodeA = llA.head
    nodeB = llB.head

    lenA = len(llA)
    lenB = len(llB)

    if(lenA == lenB):
        pass
    elif(lenA > lenB):
        diff = lenA - lenB
        for i in range(diff):
            nodeA = nodeA.next
    else:
        diff = lenB - lenA
        for i in range(diff):
            nodeB = nodeB.next
    while nodeA and nodeB:
        if nodeA.value == nodeB.value:
            return nodeA
        else:
            nodeA = nodeA.next
            nodeB = nodeB.next
    return "No intersection"


def intersection2(llA, llB):
    if llA.tail is not llB.tail:
        return False
    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA
    diff = abs(lenA - lenB)

    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    return longerNode


def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode


llA = LinkedList()
llA.generate(3, 0, 9)
llB = LinkedList()
llB.generate(5, 0, 9)


addSameNode(llA, llB, 10)
addSameNode(llA, llB, 8)
addSameNode(llA, llB, 9)

print(llA)
print(llB)
print(intersection(llA, llB))
print(intersection2(llA, llB))
