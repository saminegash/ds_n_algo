from linkedlist import LinkedList


def removeDups(ll):
    if ll.head is None:
        return "Linked list is empty"
    else:
        currNode = ll.head
        tmpSet = set([currNode.value])

        while currNode.next is not None:
            if currNode.next.value in tmpSet:
                currNode.next = currNode.next.next
            else:
                tmpSet.add(currNode.next.value)
                currNode = currNode.next
        return ll


def removeDups1(ll):
    if ll.head is None:
        return
    currNode = ll.head

    while currNode:
        runner = currNode
        while runner.next:
            if currNode.value == runner.next.value:
                currNode.next = runner.next.next
            else:
                runner = runner.next
        currNode = currNode.next
    return ll


customLL = LinkedList()
customLL.generate(10, 0, 8)
print(customLL)
print(removeDups(customLL))
print(removeDups1(customLL))
